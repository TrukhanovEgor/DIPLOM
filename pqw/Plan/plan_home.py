import flet as ft

def plan_home(page, content_area):
    content_area.controls.clear()
    content_area.controls.append(
        ft.Text("План тренировок: Комплекс для дома", size=20, weight=ft.FontWeight.BOLD)
    )
    page.update()
