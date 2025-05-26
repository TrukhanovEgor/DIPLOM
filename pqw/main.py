import flet as ft
from auth import auth_page
from database import init_db
from exemples import create_panel_exempless
from ui import create_app_bar, create_panel_plans, show_page
from journal.journal import journal_page
from Profile.profile import profile_page
from Progress.Progress import progress_page

def main(page: ft.Page):
    init_db()
    page.title = 'XFitnes'
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLACK 
    page.window.width = 350  
    page.window.height = 600 
    page.window.resizable = True

    def logout():
        page.session.clear()
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
        content_area = ft.Column(expand=True)

        # Сначала определяем go_to_plan и go_to_journal
        def go_to_plan(e=None):
            page.clean()
            page.add(app_bar)
            page.add(panel_plans)
            show_page(0, content_area, e, page, username, go_to_journal)

        def go_to_journal(e=None):
            journal_content = ft.Column()
            page.clean()
            page.add(app_bar)
            page.add(journal_content)  # <--- ДО journal_page!
            journal_page(page, journal_content, username, go_to_plan)

        panel_plans = create_panel_plans(content_area, selected_plan, username, go_to_journal)
        panel_progress = progress_page(page)
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
                show_page(0, content_area, e, page, username, go_to_journal)
            elif index == 2:
                app_bar.title = ft.Text("Журнал тренировок", size=20)
                journal_content = ft.Column()
                page.add(journal_content)  # СНАЧАЛА добавить!
                journal_page(page, journal_content, username, go_to_plan)
            elif index == 3:
                app_bar.title = ft.Text("Прогресс", size=20)
                page.add(panel_progress)
            elif index == 4:
                app_bar.title = ft.Text("Профиль", size=20)
                page.add(panel_profile)
            page.update()

        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.FITNESS_CENTER, label="Упражнения"),
                ft.NavigationBarDestination(icon=ft.Icons.EVENT, label="Планы"),
                ft.NavigationBarDestination(icon=ft.Icons.SCHEDULE, label="Журнал"),
                ft.NavigationBarDestination(icon=ft.Icons.TIMELINE, label="Прогресс"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Профиль"),
            ],
            on_change=navigate,
            bgcolor=ft.Colors.DEEP_ORANGE_300,
            selected_index=0,
        )

        page.add(panel_exemples)

    page.add(auth_page(page, on_login_success))

ft.app(target=main)