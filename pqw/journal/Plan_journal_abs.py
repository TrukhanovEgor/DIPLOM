import flet as ft

def plan_journal_abs(page, content_area):
    content_area.controls.clear()

    app_bar = ft.AppBar(
        title=ft.Text("План: Убрать живот", color=ft.colors.WHITE),
        bgcolor=ft.colors.ORANGE_400,
    )

    content = ft.Column(
        controls=[
            ft.Text("Вааая брат страница пашет планы", size=18, color=ft.colors.WHITE),
            # добавь сюда нужный тебе план тренировок
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    page.appbar = app_bar
    content_area.controls.append(content)
    page.update()
