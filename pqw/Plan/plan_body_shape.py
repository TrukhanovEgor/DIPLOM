import flet as ft

def plan_body_shape(page, content_area):
    content_area.controls.clear()
    content_area.controls.append(
        ft.Text("План тренировок: Стройное тело", size=20, weight=ft.FontWeight.BOLD)
    )
    page.update()
