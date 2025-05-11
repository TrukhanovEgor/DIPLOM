import flet as ft

def plan_push_pull(page, content_area):
    content_area.controls.clear()
    content_area.controls.append(
        ft.Text("План тренировок: Жим и Тяги", size=20, weight=ft.FontWeight.BOLD)
    )
    page.update()
