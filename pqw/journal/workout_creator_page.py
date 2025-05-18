import flet as ft
from database import save_workout

def workout_creator_page(page, content_area, username, on_workout_saved=None):
    exercises = []
    workout_name_field = ft.TextField(label="Название тренировки")

    muscle_groups = [
        "Грудные мышцы", "Бицепс", "Трицепс", "Широчайшие",
        "Трапеция", "Дельты", "Пресс", "Ноги"
    ]

    exercises_list = ft.Column()

    def update_exercises_list():
        exercises_list.controls.clear()
        if not exercises:
            exercises_list.controls.append(
                ft.Text("Нет добавленных упражнений", color=ft.colors.WHITE)
            )
        else:
            for i, ex in enumerate(exercises, 1):
                exercises_list.controls.append(
                    ft.Text(
                        f"{i}. {ex['exercise_name']} ({ex['muscle_group']}): "
                        f"{ex['sets_count']} x {ex['reps_count']}",
                        color=ft.colors.WHITE
                    )
                )

    def add_exercise_dialog(e=None):
        exercise_name = ft.TextField(label="Название упражнения")
        sets_count = ft.TextField(label="Количество подходов", keyboard_type=ft.KeyboardType.NUMBER)
        reps_count = ft.TextField(label="Количество повторений", keyboard_type=ft.KeyboardType.NUMBER)
        muscle_group_picker = ft.Dropdown(
            label="Группа мышц",
            options=[ft.dropdown.Option(mg) for mg in muscle_groups],
        )

        def save_exercise(_):
            if not all([exercise_name.value, sets_count.value, reps_count.value, muscle_group_picker.value]):
                page.snack_bar = ft.SnackBar(ft.Text("Заполните все поля упражнения!"))
                page.snack_bar.open = True
                page.update()
                return
            exercises.append({
                "exercise_name": exercise_name.value,
                "sets_count": int(sets_count.value),
                "reps_count": int(reps_count.value),
                "muscle_group": muscle_group_picker.value,
            })
            update_exercises_list()
            dialog.open = False
            page.update()

        def close_dialog(_):
            dialog.open = False
            page.update()

        dialog = ft.AlertDialog(
            title=ft.Text("Добавить упражнение"),
            content=ft.Column([
                exercise_name, sets_count, reps_count, muscle_group_picker
            ]),
            actions=[
                ft.TextButton("Добавить", on_click=save_exercise),
                ft.TextButton("Отмена", on_click=close_dialog),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        if dialog not in page.overlay:
            page.overlay.append(dialog)
        dialog.open = True
        page.update()

    def save_workout_and_exit(e=None):
        if not workout_name_field.value:
            page.snack_bar = ft.SnackBar(ft.Text("Введите название тренировки!"))
            page.snack_bar.open = True
            page.update()
            return
        if not exercises:
            page.snack_bar = ft.SnackBar(ft.Text("Добавьте хотя бы одно упражнение!"))
            page.snack_bar.open = True
            page.update()
            return
        for ex in exercises:
            save_workout(
                username=username,
                workout_name=workout_name_field.value,
                exercise_name=ex["exercise_name"],
                sets_count=ex["sets_count"],
                reps_count=ex["reps_count"],
                muscle_group=ex["muscle_group"],
            )
        # После сохранения возвращаемся в журнал
        from .journal import journal_page
        content_area.controls.clear()
        journal_page(page, content_area, username)
        page.update()
        if on_workout_saved:
            on_workout_saved()

    app_bar = ft.AppBar(
        title=ft.Text("Новая тренировка", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
        actions=[
            ft.TextButton("Сохранить", style=ft.ButtonStyle(color=ft.colors.WHITE), on_click=save_workout_and_exit)
        ]
    )

    content = ft.Column([
        workout_name_field,
        exercises_list,
        ft.ElevatedButton(
            "Добавить упражнение",
            icon=ft.icons.ADD,
            on_click=add_exercise_dialog,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.WHITE10,
                color=ft.colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=30),
            ),
        ),
    ], spacing=20, alignment=ft.MainAxisAlignment.CENTER)

    update_exercises_list()

    scrollable_content = ft.Container(
        content=ft.Column([content], alignment=ft.MainAxisAlignment.CENTER),
        expand=True,
        bgcolor=ft.colors.BLACK,
        padding=30,
    )

    page.add(app_bar)
    content_area.controls.append(scrollable_content)
    page.update()