import flet as ft
from database import delete_workout_from_db, get_user_workouts
from .workout_creator_page import workout_creator_page
from .Plan_journal_abs import plan_journal_abs

def journal_page(page, content_area, username, go_to_plan):
    if page is None:
        return

    content_area.controls.clear()

    app_bar = ft.AppBar(
        title=ft.Text("Журнал тренировок", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

    show_plan_button = {"value": True}

    def toggle_visibility(tile):
        tile.subtitle.visible = not tile.subtitle.visible
        page.update()

    def get_grouped_workouts():
        all_w = get_user_workouts(username)
        grouped = {}
        for w in all_w:
            workout_name = w[0]
            exercise_info = w[1:]
            grouped.setdefault(workout_name, []).append(exercise_info)
        return grouped

    def remove_plan_button(e=None):
        show_plan_button["value"] = False
        refresh_workouts()

    def create_tile(workout_name, exercises):
        if workout_name == "Убрать живот" and show_plan_button["value"]:
            tile = ft.Row(
                [
                    ft.ElevatedButton(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.FITNESS_CENTER, size=24, color=ft.colors.WHITE),
                                ft.Text("План: Убрать живот", size=18, weight=ft.FontWeight.BOLD),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,
                        ),
                        on_click=lambda e: plan_journal_abs(page, content_area),

                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.ORANGE_400,
                            color=ft.colors.WHITE,
                            shape=ft.RoundedRectangleBorder(radius=20),
                            padding=ft.padding.symmetric(horizontal=20, vertical=16),
                            shadow_color=ft.colors.ORANGE_800,
                            elevation=8,
                            overlay_color=ft.colors.ORANGE_200
                        ),
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color=ft.colors.RED,
                        tooltip="Удалить план",
                        on_click=remove_plan_button,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=12),
                            padding=ft.padding.all(10),
                            bgcolor=ft.colors.RED_100,
                            overlay_color=ft.colors.RED_200,
                        ),
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            )
            return tile
        elif workout_name == "Убрать живот" and not show_plan_button["value"]:
            return None

        # Обычные тренировки
        start_time, end_time, duration = exercises[0][4], exercises[0][5], exercises[0][6]
        subtitle_controls = []
        if duration is not None:
            h = int(duration) // 3600
            m = (int(duration) % 3600) // 60
            s = int(duration) % 60
            subtitle_controls.append(
                ft.Text(f"Время тренировки: {h:02}:{m:02}:{s:02}", color=ft.colors.AMBER_100)
            )
        for exercise_name, sets_count, reps_count, muscle_group, *_ in exercises:
            subtitle_controls.append(
                ft.Text(f"{exercise_name} | {sets_count} x {reps_count} | {muscle_group}", color=ft.colors.WHITE)
            )
        tile = ft.ListTile(
            title=ft.Text(f"{workout_name}", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            subtitle=ft.Column(subtitle_controls, visible=False),
            bgcolor=ft.colors.GREY_900,
            on_click=lambda e: toggle_visibility(tile),
            trailing=ft.IconButton(
                icon=ft.icons.DELETE,
                icon_color=ft.colors.RED,
                on_click=lambda e: delete_whole_workout(workout_name)
            ),
        )
        return tile

    def delete_whole_workout(workout_name):
        all_w = get_user_workouts(username)
        for w in all_w:
            if w[0] == workout_name:
                delete_workout_from_db(username, *w[:5])
        refresh_workouts()

    def refresh_workouts():
        workouts_list.controls.clear()
        grouped = get_grouped_workouts()
        for workout_name, exercises in grouped.items():
            tile = create_tile(workout_name, exercises)
            if tile is not None:
                workouts_list.controls.append(tile)
        page.update()

    workouts_list = ft.ListView(controls=[], width=None, height=500, spacing=10)

    muscle_groups = ["Все", "Грудные мышцы", "Бицепс", "Трицепс", "Широчайшие", "Трапеция", "Дельты", "Пресс", "Ноги"]
    filter_dropdown = ft.Dropdown(
        label="Фильтр по группе мышц",
        options=[ft.dropdown.Option(mg) for mg in muscle_groups],
        value="Все",
        on_change=lambda e: apply_filter(),
    )

    def apply_filter():
        workouts_list.controls.clear()
        grouped = get_grouped_workouts()
        selected_filter = filter_dropdown.value
        for workout_name, exercises in grouped.items():
            tile = create_tile(workout_name, exercises)
            if tile is not None:
                if selected_filter == "Все" or any(ex[3] == selected_filter for ex in exercises):
                    workouts_list.controls.append(tile)
        page.update()

    def go_to_create_workout(_):
        content_area.controls.clear()
        page.update()
        workout_creator_page(page, content_area, username, on_workout_saved=refresh_workouts)

    start_workout_button = ft.ElevatedButton(
        "Начать тренировку",
        icon=ft.icons.ADD,
        on_click=go_to_create_workout,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.DEEP_ORANGE_300,
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=15),
        ),
    )

    content = ft.Column(
        controls=[],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    scrollable_content = ft.ListView(
        controls=[content],
        spacing=20,
        expand=True,
    )

    page.add(app_bar)
    content_area.controls.append(scrollable_content)
    page.update()

    def rebuild_content():
        content.controls.clear()
        content.controls.append(
            ft.Row([filter_dropdown], alignment=ft.MainAxisAlignment.CENTER)
        )
        content.controls.append(start_workout_button)
        content.controls.append(workouts_list)
        content.update()

    refresh_workouts()
    rebuild_content()
