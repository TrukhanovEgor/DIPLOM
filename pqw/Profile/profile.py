import flet as ft

def profile_page(page, logout_callback):
    def go_back(e):
        page.go_back()

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
            ft.Text("Пользователь", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text("Тренировок: 0 • С нами: 0 дней", size=14, color=ft.colors.GREY_400),
            ft.Row(
                [
                    ft.Column([ft.Text("0", size=20, weight=ft.FontWeight.BOLD), ft.Text("Тренировок")], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Column([ft.Text("0", size=20, weight=ft.FontWeight.BOLD), ft.Text("Упражнений")], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Column([ft.Text("0", size=20, weight=ft.FontWeight.BOLD), ft.Text("Подходов")], alignment=ft.MainAxisAlignment.CENTER),
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
                leading=ft.Icon(ft.icons.SETTINGS),
                title=ft.Text("Настройки приложения"),
                on_click=lambda _: page.snack_bar.open(ft.Text("Настройки пока не реализованы"))
            ),
            ft.ListTile(
                leading=ft.Icon(ft.icons.INFO),
                title=ft.Text("О приложении"),
                on_click=lambda _: page.snack_bar.open(ft.Text("Это фитнес-приложение для отслеживания тренировок"))
            ),
            ft.ListTile(
                leading=ft.Icon(ft.icons.STAR),
                title=ft.Text("Оценить приложение"),
                on_click=lambda _: page.snack_bar.open(ft.Text("Спасибо за оценку!"))
            ),
            ft.ListTile(
                leading=ft.Icon(ft.icons.WORKSPACE_PREMIUM),
                title=ft.Text("Премиум версия"),
                on_click=lambda _: page.snack_bar.open(ft.Text("Скоро доступно!"))
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
