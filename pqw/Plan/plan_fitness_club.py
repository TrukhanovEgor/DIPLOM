import flet as ft

def plan_fitness_club(page, content_area):
    content_area.controls.clear()
    content_area.controls.append(
        ft.Text("План тренировок: Фитнес клуб", size=20, weight=ft.FontWeight.BOLD)
    )
    page.update()
