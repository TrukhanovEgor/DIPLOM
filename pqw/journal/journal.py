import flet as ft

def journal_page(page, content_area):
    if page is None:
        return

    # Очистка только content_area
    content_area.controls.clear()

    def go_back(e):
        # Implement the back navigation logic here
        page.go_back()  # Assuming go_back() is a method to navigate back

    app_bar = ft.AppBar(
        title=ft.Text("Журнал тренировок", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
        leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=go_back),  # Add back button
    )

    # Создаем контейнер для добавления новой тренировки
    add_workout_button = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Добавить тренировку",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=10,
        bgcolor=ft.colors.DEEP_ORANGE_300,
        border_radius=15,
        width=200,
        height=50,
        on_click=lambda _: show_add_workout_dialog(page),
    )

    # Функция отображения диалога добавления тренировки
    def show_add_workout_dialog(page):
        workout_name = ft.TextField(label="Название тренировки")
        exercise_name = ft.TextField(label="Название упражнения")
        sets_count = ft.TextField(label="Количество подходов", keyboard_type=ft.KeyboardType.NUMBER)
        reps_count = ft.TextField(label="Количество повторений", keyboard_type=ft.KeyboardType.NUMBER)
        
        muscle_groups = ["Грудные мышцы", "Бицепс", "Трицепс", "Широчайшие", "Трапеция", "Дельты", "Пресс", "Ноги"]
        muscle_group_picker = ft.Dropdown(
            label="Группа мышц",
            options=[ft.dropdown.Option(mg) for mg in muscle_groups]
        )

        def add_workout(e):
            workout_content = ft.ListTile(
                title=ft.Text(
                    f"Тренировка: {workout_name.value}",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                ),
                subtitle=ft.Column(
                    [
                        ft.Text(
                            f"Упражнение: {exercise_name.value}",
                            size=14,
                            color=ft.colors.WHITE,
                        ),
                        ft.Text(
                            f"Подходы: {sets_count.value}",
                            size=14,
                            color=ft.colors.WHITE,
                        ),
                        ft.Text(
                            f"Повторения: {reps_count.value}",
                            size=14,
                            color=ft.colors.WHITE,
                        ),
                        ft.Text(
                            f"Группа мышц: {muscle_group_picker.value}",
                            size=14,
                            color=ft.colors.WHITE,
                        ),
                    ],
                    visible=False,  # Изначально скрываем подробности
                ),
                bgcolor=ft.colors.GREY_900,  # Устанавливаем серый фон
                on_click=lambda _: toggle_visibility(workout_content)
            )
            workouts_list.controls.append(workout_content)
            page.dialog.open = False  # Закрываем диалог после добавления тренировки
            page.update()

        def toggle_visibility(tile):
            tile.subtitle.visible = not tile.subtitle.visible
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

    # Список тренировок
    workouts_list = ft.ListView(
        controls=[],
        width=None,
        height=600,
        spacing=10,
    )

    # Контейнер для добавления тренировок и списка тренировок
    content = ft.Column(
        controls=[add_workout_button, workouts_list],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Заменяем ScrollContainer на ListView для поддержки прокрутки
    scrollable_content = ft.ListView(
        controls=[content],
        spacing=20,
        expand=True,
    )

    page.add(app_bar)
    content_area.controls.append(scrollable_content)
    page.update()