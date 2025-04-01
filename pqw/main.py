import flet as ft
from exemples import create_panel_exempless
from ui import create_app_bar, create_panel_plans, show_page
from journal.journal import journal_page

def main(page: ft.Page):
    page.title = 'XFitnes'
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK
    page.window.width = 350  
    page.window.height = 600 
    page.window.resizable = True 
    
    app_bar = create_app_bar()
    page.add(app_bar)

    panel_exemples = create_panel_exempless(page)
    
    selected_plan = ft.Text(size=24, weight=ft.FontWeight.BOLD)
    content_area = ft.Column()

    
    panel_plans = create_panel_plans(content_area, selected_plan)

    # Журнал
    panel_journal_content = ft.Column()
    journal_page(page, panel_journal_content)

    # Профиль
    panel_profile = ft.Row([ft.Text("Профиль")])

    def navigate(e):
        index = e.control.selected_index
        page.clean() 

      
        if index == 0:
            app_bar.title = ft.Text("Упражнения", size=20)
            page.add(panel_exemples)
        elif index == 1:
            app_bar.title = ft.Text("Планы", size=20)
            page.add(panel_plans) 
            show_page(0, content_area, e, page)  # Показать первую страницу по умолчанию
        elif index == 2:
            app_bar.title = ft.Text("Журнал", size=20)
            page.add(panel_journal_content)
        elif index == 3:
            app_bar.title = ft.Text("Профиль", size=20)
            page.add(panel_profile)

        page.add(app_bar)  
        page.update() 

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.FITNESS_CENTER, label="Упражнения"),
            ft.NavigationBarDestination(icon=ft.icons.EVENT, label="Планы"),
            ft.NavigationBarDestination(icon=ft.icons.SCHEDULE, label="Журнал"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Профиль"),
        ],
        on_change=navigate,
        bgcolor=ft.colors.DEEP_ORANGE_300,
        selected_index=0,
    )
    
    page.add(panel_exemples)  # Добавляем начальный экран "Упражнения"

ft.app(target=main)