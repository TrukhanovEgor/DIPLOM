import flet as ft
from database import save_workout
import sqlite3
from datetime import datetime

def plan_journal_fitness_club(page: ft.Page, content_area: ft.Column, username, refresh_journal, go_back):
    print("Загрузка страницы Журнал плана 'Фитнес-клуб'")  # Отладка
    content_area.controls.clear()

    app_bar = ft.AppBar(
        title=ft.Text("План: Фитнес-клуб", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
        bgcolor=ft.Colors.DEEP_ORANGE_300,
        leading=ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.WHITE,
            on_click=go_back,
            tooltip="Назад",
        ),
        actions=[
            ft.IconButton(
                icon=ft.Icons.BOOK,
                icon_color=ft.Colors.WHITE,
                on_click=refresh_journal,
                tooltip="Перейти в журнал",
            ),
        ],
    )

    def get_progress():
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT exercise_name FROM workouts
            WHERE username = ? AND workout_name = 'Фитнес-клуб'
        """, (username,))
        completed = set(row[0] for row in cursor.fetchall())
        conn.close()
        return completed

    # План: 8 недель × 3 тренировки в неделю
    total_workouts = 8 * 3
    completed_workouts = get_progress()
    completed_count = len(completed_workouts)
    progress_percentage = (completed_count / total_workouts) * 100 if total_workouts > 0 else 0

    progress_container = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Прогресс плана",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.ProgressRing(
                    value=progress_percentage / 100,
                    color=ft.Colors.DEEP_ORANGE_300,
                    bgcolor=ft.Colors.GREY_700,
                    width=100,
                    height=100,
                ),
                ft.Text(
                    f"{completed_count} из {total_workouts} тренировок ({progress_percentage:.1f}%)",
                    size=14,
                    color=ft.Colors.WHITE70,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        padding=ft.padding.all(15),
        bgcolor=ft.Colors.GREY_800,
        border_radius=12,
        margin=ft.margin.symmetric(horizontal=10, vertical=10),
        shadow=ft.BoxShadow(
            blur_radius=8,
            spread_radius=1,
            offset=ft.Offset(0, 4),
            color=ft.Colors.BLACK26,
        ),
    )

    # Словарь с заданиями для каждого дня недели
    day_tasks = {
        1: [  # День 1: Грудь + Трицепс
            "Жим штанги лёжа: 3x8–12",
            "Жим гантелей на наклонной скамье: 3x10–12",
            "Разводка гантелей: 3x12–15",
            "Французский жим: 3x10–12",
            "Разгибания на блоке: 3x12–15",
            "Отжимания на брусьях: 3x10–12",
        ],
        2: [  # День 2: Спина + Бицепс
            "Подтягивания: 3x6–10",
            "Тяга штанги в наклоне: 3x8–12",
            "Тяга верхнего блока: 3x10–12",
            "Сгибания со штангой: 3x10–12",
            "Сгибания с гантелями (молот): 3x12–15",
            "Концентрированные сгибания: 3x12–15",
        ],
        3: [  # День 3: Ноги + Плечи
            "Приседания со штангой: 3x8–12",
            "Жим ногами: 3x10–12",
            "Выпады с гантелями: 3x12 на ногу",
            "Жим штанги стоя: 3x8–12",
            "Подъёмы гантелей через стороны: 3x12–15",
            "Тяга штанги к подбородку: 3x10–12",
        ],
    }

    def create_workout_card(week, day):
        exercise_name = f"День {day}: Неделя {week}"
        is_completed = exercise_name in completed_workouts

        def on_checkbox_change(e):
            if e.control.value:
                save_workout(
                    username=username,
                    workout_name="Фитнес-клуб",
                    exercise_name=exercise_name,
                    sets_count="-",
                    reps_count="-",
                    muscle_group="План",
                    start_time=datetime.now().isoformat(),
                    end_time=None,
                    duration=None,
                )
                completed_workouts.add(exercise_name)
            else:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
                cursor.execute("""
                    DELETE FROM workouts
                    WHERE username = ? AND workout_name = ? AND exercise_name = ?
                """, (username, "Фитнес-клуб", exercise_name))
                conn.commit()
                conn.close()
                completed_workouts.discard(exercise_name)

            new_completed_count = len(completed_workouts)
            new_progress_percentage = (new_completed_count / total_workouts) * 100
            progress_container.content.controls[2].value = (
                f"{new_completed_count} из {total_workouts} тренировок ({new_progress_percentage:.1f}%)"
            )
            progress_container.content.controls[1].value = new_progress_percentage / 100
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Тренировка '{exercise_name}' {'отмечена как выполненная' if e.control.value else 'удалена'}")
            )
            page.snack_bar.open = True
            page.update()

        # Получаем упражнения для этого дня
        exercises = day_tasks[day]

        return ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Checkbox(
                                value=is_completed,
                                on_change=on_checkbox_change,
                                check_color=ft.Colors.WHITE,
                                fill_color=ft.Colors.GREEN_400,
                            ),
                            ft.Text(
                                exercise_name,
                                size=14,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Text(
                        "\n".join(exercises),
                        size=12,
                        color=ft.Colors.WHITE70,
                        text_align=ft.TextAlign.LEFT,
                    ),
                ],
                spacing=8,
            ),
            padding=ft.padding.all(10),
            bgcolor=ft.Colors.GREY_900,
            border_radius=8,
            margin=ft.margin.symmetric(horizontal=10, vertical=5),
            shadow=ft.BoxShadow(
                blur_radius=6,
                spread_radius=1,
                offset=ft.Offset(0, 3),
                color=ft.Colors.BLACK26,
            ),
        )

    workout_cards = []
    for week in range(1, 9):
        week_container = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        f"Неделя {week}",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREEN_400,
                    ),
                    create_workout_card(week, 1),
                    create_workout_card(week, 2),
                    create_workout_card(week, 3),
                ],
                spacing=8,
            ),
            padding=ft.padding.symmetric(vertical=10),
        )
        workout_cards.append(week_container)

    content = ft.Column(
        controls=[
            progress_container,
            ft.Text(
                "Отмечайте выполненные тренировки",
                size=14,
                color=ft.Colors.WHITE,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Column(
                controls=workout_cards,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=15,
        expand=True,
    )

    content_area.controls.append(
        ft.Container(
            content=content,
            padding=ft.padding.symmetric(horizontal=10, vertical=5),
            height=page.height - 100 if page.height else 600,
            expand=True,
            bgcolor=ft.Colors.BLACK,
        )
    )

    page.appbar = app_bar
    content_area.expand = True
    page.update()