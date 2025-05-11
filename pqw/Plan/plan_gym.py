import flet as ft

def plan_gym(page, content_area):
    content_area.controls.clear()
    content_area.controls.append(
        ft.Text("План тренировок: Домашний спортзал", size=20, weight=ft.FontWeight.BOLD)
    )
    page.update()
