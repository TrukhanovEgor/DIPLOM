import flet as ft
from database import save_workout
from datetime import datetime
import threading
import time

def workout_creator_page(page, content_area, username, on_workout_saved=None):
  
    exercises = []
    workout_name_field = ft.TextField(label="Название тренировки")
    muscle_groups = [
        "Грудные мышцы", "Бицепс", "Трицепс", "Широчайшие",
        "Трапеция", "Дельты", "Пресс", "Ноги"
    ]
    exercises_list = ft.Column()

    # Таймер переменные
    timer_value = ft.Text("00:00:00", size=32, color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER)
    timer_seconds = [0]
    timer_started_time = [None]
    timer_ended_time = [None]
    timer_is_running = [False]
    timer_thread = [None]
    stop_signal = [False]

    def timer_worker():
        while timer_is_running[0]:
            time.sleep(1)
            if not timer_is_running[0]:
                break
            timer_seconds[0] = int((datetime.now() - timer_started_time[0]).total_seconds())
            h = timer_seconds[0] // 3600
            m = (timer_seconds[0] % 3600) // 60
            s = timer_seconds[0] % 60
            timer_value.value = f"{h:02}:{m:02}:{s:02}"
            page.update()

    def start_timer(*_):
        if not timer_is_running[0]:
            timer_is_running[0] = True
            timer_started_time[0] = datetime.now()
            timer_thread[0] = threading.Thread(target=timer_worker, daemon=True)
            timer_thread[0].start()
            page.update()

    def stop_timer(*_):
        if timer_is_running[0]:
            timer_is_running[0] = False
            timer_ended_time[0] = datetime.now()
            page.update()

    def reset_timer(*_):
        timer_is_running[0] = False
        timer_seconds[0] = 0
        timer_started_time[0] = None
        timer_ended_time[0] = None
        timer_value.value = "00:00:00"
        page.update()

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
        stop_timer()
        start_str = timer_started_time[0].strftime("%Y-%m-%d %H:%M:%S") if timer_started_time[0] else None
        end_str = timer_ended_time[0].strftime("%Y-%m-%d %H:%M:%S") if timer_ended_time[0] else None
        duration = timer_seconds[0]
        for ex in exercises:
            save_workout(
                username=username,
                workout_name=workout_name_field.value,
                exercise_name=ex["exercise_name"],
                sets_count=ex["sets_count"],
                reps_count=ex["reps_count"],
                muscle_group=ex["muscle_group"],
                start_time=start_str,
                end_time=end_str,
                duration=duration
            )
        from .journal import journal_page
        content_area.controls.clear()
        journal_page(page, content_area, username)
        page.update()
        if on_workout_saved:
            on_workout_saved()

    def cancel_workout(e=None):
        # Остановить таймер, очистить поля, перейти обратно в журнал
        stop_timer()
        from .journal import journal_page
        content_area.controls.clear()
        journal_page(page, content_area, username)
        page.update()

    app_bar = ft.AppBar(
        title=ft.Text("Новая тренировка", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
        actions=[
            ft.TextButton("Сохранить", style=ft.ButtonStyle(color=ft.colors.WHITE), on_click=save_workout_and_exit),
            ft.TextButton("Отмена", style=ft.ButtonStyle(color=ft.colors.WHITE), on_click=cancel_workout)
        ]
    )

    def cancel_workout(e=None):
        confirm_dialog = ft.AlertDialog(
            title=ft.Text("Отмена тренировки"),
            content=ft.Text("Вы уверены, что хотите отменить тренировку? Введённые данные будут утеряны."),
            actions=[
                ft.TextButton("Да", on_click=lambda e: do_cancel()),
                ft.TextButton("Нет", on_click=lambda e: close_dialog())
            ]
        )

        def do_cancel():
            stop_timer()
            from .journal import journal_page
            content_area.controls.clear()
            journal_page(page, content_area, username)
            confirm_dialog.open = False
            page.update()

        def close_dialog():
            confirm_dialog.open = False
            page.update()

        if confirm_dialog not in page.overlay:
            page.overlay.append(confirm_dialog)
        confirm_dialog.open = True
        page.update()


    timer_buttons = ft.Row([
        ft.ElevatedButton("Старт", on_click=start_timer),
        ft.ElevatedButton("Сброс", on_click=reset_timer),
    ], alignment=ft.MainAxisAlignment.CENTER)

    content = ft.Column([
        workout_name_field,
        ft.Container(
            ft.Column([
                timer_value,
                timer_buttons,
            ], alignment=ft.MainAxisAlignment.CENTER),
            alignment=ft.alignment.center,
            padding=20,
        ),
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