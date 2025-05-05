import flet as ft
from database import save_workout, get_user_workouts

def journal_page(page, content_area, username):
    if page is None:
        return

    content_area.controls.clear()


    app_bar = ft.AppBar(
        title=ft.Text("Журнал тренировок", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
        
    )

    def toggle_visibility(tile):
        tile.subtitle.visible = not tile.subtitle.visible
        page.update()

    def create_tile(workout_name, exercise_name, sets_count, reps_count, muscle_group):
        return ft.ListTile(
            title=ft.Text(f"Тренировка: {workout_name}", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            subtitle=ft.Column([
                ft.Text(f"Упражнение: {exercise_name}", size=14, color=ft.colors.WHITE),
                ft.Text(f"Подходы: {sets_count}", size=14, color=ft.colors.WHITE),
                ft.Text(f"Повторения: {reps_count}", size=14, color=ft.colors.WHITE),
                ft.Text(f"Группа мышц: {muscle_group}", size=14, color=ft.colors.WHITE),
            ], visible=False),
            bgcolor=ft.colors.GREY_900,
            on_click=lambda e: toggle_visibility(),
            trailing=ft.IconButton(
                icon=ft.icons.DELETE,
                icon_color=ft.colors.RED,
                on_click=lambda e: delete_workout(
                    workout_name=workout_name,
                    exercise_name=exercise_name,
                    sets_count=sets_count,
                    reps_count=reps_count,
                    muscle_group=muscle_group
                )
            ),
        )

    def delete_workout(workout_name, exercise_name, sets_count, reps_count, muscle_group):
        # Предполагаемая функция удаления (нужно реализовать в database.py)
        # delete_workout_from_db(username, workout_name, exercise_name, sets_count, reps_count, muscle_group)
        print(f"Удаление тренировки: {workout_name}, {exercise_name}")
        refresh_workouts()  # Обновляем список после удаления

    def refresh_workouts():
        workouts_list.controls.clear()
        for workout in get_user_workouts(username):
            workout_name, exercise_name, sets_count, reps_count, muscle_group = workout
            tile = create_tile(workout_name, exercise_name, sets_count, reps_count, muscle_group)
            workouts_list.controls.append(tile)
        page.update()

    workouts_list = ft.ListView(controls=[], width=None, height=500, spacing=10)

    # Фильтрация по группе мышц
    muscle_groups = ["Все", "Грудные мышцы", "Бицепс", "Трицепс", "Широчайшие", "Трапеция", "Дельты", "Пресс", "Ноги"]
    filter_dropdown = ft.Dropdown(
        label="Фильтр по группе мышц",
        options=[ft.dropdown.Option(mg) for mg in muscle_groups],
        value="Все",
        on_change=lambda e: apply_filter(),
    )

    def apply_filter():
        workouts_list.controls.clear()
        workouts = get_user_workouts(username)
        selected_filter = filter_dropdown.value
        if selected_filter != "Все":
            workouts = [w for w in workouts if w[4] == selected_filter]  # w[4] — muscle_group
        for workout in workouts:
            workout_name, exercise_name, sets_count, reps_count, muscle_group = workout
            tile = create_tile(workout_name, exercise_name, sets_count, reps_count, muscle_group)
            workouts_list.controls.append(tile)
        page.update()

    def show_add_workout_dialog(page):
        workout_name = ft.TextField(label="Название тренировки")
        exercise_name = ft.TextField(label="Название упражнения")
        sets_count = ft.TextField(label="Количество подходов", keyboard_type=ft.KeyboardType.NUMBER)
        reps_count = ft.TextField(label="Количество повторений", keyboard_type=ft.KeyboardType.NUMBER)
        muscle_group_picker = ft.Dropdown(
            label="Группа мышц",
            options=[ft.dropdown.Option(mg) for mg in muscle_groups[1:]],  # Исключаем "Все"
        )

        def add_workout(e):
            if not all([workout_name.value, exercise_name.value, sets_count.value, reps_count.value, muscle_group_picker.value]):
                page.snack_bar = ft.SnackBar(ft.Text("Заполните все поля!"))
                page.snack_bar.open = True
                page.update()
                return

            save_workout(
                username=username,
                workout_name=workout_name.value,
                exercise_name=exercise_name.value,
                sets_count=int(sets_count.value),
                reps_count=int(reps_count.value),
                muscle_group=muscle_group_picker.value,
            )
            page.dialog.open = False
            refresh_workouts()  # Обновляем список после добавления
            page.update()

        def close_dialog(e):
            page.dialog.open = False
            page.update()

        page.dialog = ft.AlertDialog(
            title=ft.Text("Добавить тренировку"),
            content=ft.Column(
                [
                    workout_name,
                    exercise_name,
                    sets_count,
                    reps_count,
                    muscle_group_picker,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            actions=[
                ft.TextButton("Добавить", on_click=add_workout),
                ft.TextButton("Отмена", on_click=close_dialog),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog.open = True
        page.update()

    add_workout_button = ft.ElevatedButton(
        "Добавить тренировку",
        icon=ft.icons.ADD,
        on_click=lambda _: show_add_workout_dialog(page),
        style=ft.ButtonStyle(
            bgcolor=ft.colors.DEEP_ORANGE_300,
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=15),
        ),
    )

    content = ft.Column(
        controls=[
            ft.Row([filter_dropdown], alignment=ft.MainAxisAlignment.CENTER),
            add_workout_button,
            workouts_list,
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    scrollable_content = ft.ListView(
        controls=[content],
        spacing=20,
        expand=True,
    )

    # Инициализация списка тренировок
    refresh_workouts()

    page.add(app_bar)
    content_area.controls.append(scrollable_content)
    page.update()
