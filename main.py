import flet as ft
from auth import auth_page
from database import init_db
from exemples import create_panel_exempless
from ui import create_app_bar, create_panel_plans, show_page
from journal.journal import journal_page
from Profile.profile import profile_page

def main(page: ft.Page):
    init_db()
    page.title = 'XFitnes'
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLACK  # Исправлено: colors -> Colors
    page.window.width = 350  
    page.window.height = 600 
    page.window.resizable = True

    def logout():
        page.session.clear()  # очищаем сохранённое имя пользователя
        page.clean()
        page.navigation_bar = None
        page.add(auth_page(page, on_login_success))

    def on_login_success(username):
        page.session.set("username", username)
        page.clean()

        app_bar = create_app_bar()
        page.add(app_bar)

        panel_exemples = create_panel_exempless(page)
        selected_plan = ft.Text(size=24, weight=ft.FontWeight.BOLD)
        content_area = ft.Column()
        panel_plans = create_panel_plans(content_area, selected_plan)

        # Профиль
        panel_profile = profile_page(page, logout_callback=logout, username=username)

        def navigate(e):
            index = e.control.selected_index
            page.clean()
            page.add(app_bar)

            if index == 0:
                app_bar.title = ft.Text("Упражнения", size=20)
                page.add(panel_exemples)
            elif index == 1:
                app_bar.title = ft.Text("Планы", size=20)
                page.add(panel_plans)
                show_page(0, content_area, e, page)
            elif index == 2:
                app_bar.title = ft.Text("Журнал тренировок", size=20)
                journal_content = ft.Column()
                journal_page(page, journal_content, username)
                page.add(journal_content)
            elif index == 3:
                app_bar.title = ft.Text("Профиль", size=20)
                page.add(panel_profile)

            page.update()

        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.FITNESS_CENTER, label="Упражнения"),  # Исправлено: icons -> Icons
                ft.NavigationBarDestination(icon=ft.Icons.EVENT, label="Планы"),  # Исправлено: icons -> Icons
                ft.NavigationBarDestination(icon=ft.Icons.SCHEDULE, label="Журнал"),  # Исправлено: icons -> Icons
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Профиль"),  # Исправлено: icons -> Icons
            ],
            on_change=navigate,
            bgcolor=ft.Colors.DEEP_ORANGE_300,  # Исправлено: colors -> Colors
            selected_index=0,
        )

        page.add(panel_exemples)

    page.add(auth_page(page, on_login_success))

ft.app(target=main)