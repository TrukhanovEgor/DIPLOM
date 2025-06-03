import flet as ft
from database import get_user_statistics 
from .measurements import measurements
from .Settings import settings_page

def profile_page(page, logout_callback, username, ):
    def go_back(e):
        page.go_back()
    content_area = ft.Column()
    page.add(content_area) 
    # Получаем статистику из базы
    workout_count, exercise_count, total_sets = get_user_statistics(username)

    app_bar = ft.AppBar(
        title=ft.Text("Профиль", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
        leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=go_back),
    )
    
    user_info = ft.Column(
        controls=[
            ft.Container(
                content=ft.Icon(name=ft.icons.PERSON, size=60, color=ft.colors.WHITE),
                alignment=ft.alignment.center,
                padding=10
            ),
            ft.Text(username, size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text(f"Тренировок: {workout_count} • С нами: 0 дней", size=14, color=ft.colors.GREY_400),
            ft.Row(
                [
                    ft.Column([ft.Text(str(workout_count), size=20, weight=ft.FontWeight.BOLD), ft.Text("Тренировок")], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Column([ft.Text(str(exercise_count), size=20, weight=ft.FontWeight.BOLD), ft.Text("Упражнений")], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Column([ft.Text(str(total_sets), size=20, weight=ft.FontWeight.BOLD), ft.Text("Подходов")], alignment=ft.MainAxisAlignment.CENTER),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                spacing=20,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    settings = ft.Column(
        controls=[
            ft.ListTile(
                leading=ft.Icon(ft.icons.BAR_CHART_SHARP),
                title=ft.Text("Замеры"),
                on_click=lambda e: measurements(
                    page=page,
                    logout_callback=logout_callback,
                    username=username,
                    return_to_profile=lambda: page.add(profile_page(page, logout_callback, username))
                ),
            ),

            ft.ListTile(
                leading=ft.Icon(ft.icons.SETTINGS),
                title=ft.Text("Настройки"),
                on_click=lambda e: (
                    page.controls.clear(),
                    page.add(settings_page(
                        page=page,
                        username=username,  # <-- обязательно!
                        return_to_profile=lambda: profile_page(page, logout_callback, username),
                        on_logout=logout_callback
                    )),
                    page.update()
            ),
        ),
        ],
        spacing=5
    )

    logout_button = ft.Container(
        content=ft.ElevatedButton(
            "Выйти",
            icon=ft.icons.LOGOUT,
            on_click=lambda _: logout_callback()
        ),
        padding=10,
        alignment=ft.alignment.center
    )

    layout = ft.Column(
        controls=[
            user_info,
            ft.Divider(),
            settings,
            logout_button
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
        alignment=ft.MainAxisAlignment.START,
    )

    scrollable = ft.ListView(
        controls=[layout],
        spacing=10,
        expand=True,
        padding=10
    )

    return scrollable