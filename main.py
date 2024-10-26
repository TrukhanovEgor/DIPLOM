import flet as ft

def main(page: ft.Page):
    page.title = 'APP'
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK
    page.window_width = 350
    page.window_height = 600
    page.window_resizable = False
    
    # Изначальный заголовок
    app_bar = ft.AppBar(
        title=ft.Text("Упражнения", size=30, weight=ft.FontWeight.BOLD,
                      color=ft.colors.WHITE, style="font-family: 'Arial';"),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

    page.add(app_bar)

    # Упражнение
    panel_exemples = ft.Row(
        [
            ft.Text("Упражнения"),
        ]
    )
    
    # План
    selected_plan = ft.Text(size=24, weight=ft.FontWeight.BOLD)

    # Создаем content_area для отображения страниц
    content_area = ft.Column()

    def create_panel_plan():
        return ft.Column(
            [
                ft.Container(
                    content=ft.CupertinoSlidingSegmentedButton(
                        selected_index=0,
                        thumb_color=ft.colors.DEEP_ORANGE_300,
                        on_change=lambda e: show_page(e.control.selected_index),
                        padding=ft.padding.symmetric(0, 10),
                        controls=[
                            ft.Text("Тренировки", size=20, weight=ft.FontWeight.BOLD),
                            ft.Text("Личные", size=20, weight=ft.FontWeight.BOLD),
                        ],
                    ),
                    padding=ft.padding.symmetric(0, 10),
                ),
                selected_plan,
                content_area  # Добавляем content_area сюда
            ]
        )

    panel_plans = create_panel_plan()

    # Функция для отображения содержимого страниц
    def show_page(selected_index):
        content_area.controls.clear()  # Очищаем предыдущий контент
        if selected_index == 0:
            content_area.controls.append(
                ft.Column(
                    [
                        ft.Text("Содержимое страницы Тренировки", size=20),
                        ft.Text("Здесь можно добавить больше информации о тренировках.", size=16),
                    ]
                )
            )
        elif selected_index == 1:
            # Размещаем иконки в ряд справа сверху
            content_area.controls.append(
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    icon_color="DEEP_ORANGE_300",
                                    icon_size=20,
                                    tooltip="Редактировать",
                                ),
                                ft.IconButton(
                                    icon=ft.icons.ADD_CIRCLE,
                                    icon_color="DEEP_ORANGE_300",
                                    icon_size=40,
                                    tooltip="Добавить",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,  # Выровнять по правому краю
                            spacing=10,  # Промежуток между иконками
                        ),
                        ft.Text("Содержимое страницы Личные", size=20),
                        ft.Text("Здесь можно добавить больше информации о личных планах.", size=16),
                    ]
                )
            )
        page.update()

    # Журнал
    panel_journal = ft.Row(
        [
            ft.Text("Журнал"),
        ]
    ) 
    
    # Профиль
    panel_profile = ft.Row(
        [
            ft.Text("Профиль"),
        ]
    )

    # Функция навигации
    def navigate(e):
        index = e.control.selected_index
        page.clean()

        # Обновление заголовка в зависимости от выбранной вкладки
        if index == 0:
            app_bar.title = ft.Text("Упражнения", size=20)
            page.add(panel_exemples)
        elif index == 1:
            app_bar.title = ft.Text("Планы", size=20)
            page.add(panel_plans)
            show_page(0)  # Показать первую страницу по умолчанию
        elif index == 2:
            app_bar.title = ft.Text("Журнал", size=20)
            page.add(panel_journal)
        elif index == 3:
            app_bar.title = ft.Text("Профиль", size=20)
            page.add(panel_profile)

        # Добавление шапки после очистки страницы
        page.add(app_bar)
        page.update()

    # Навигационная панель
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.FITNESS_CENTER, 
                label="Упражнения"
            ),
            ft.NavigationDestination(
                icon=ft.icons.EVENT, 
                label="Планы"
            ),
            ft.NavigationDestination(
                icon=ft.icons.SCHEDULE, 
                label="Журнал"
            ),
            ft.NavigationDestination(
                icon=ft.icons.PERSON, 
                label="Профиль"
            ),
        ],
        on_change=navigate,
        bgcolor=ft.colors.DEEP_ORANGE_300,  # Цвет фона панели
        selected_index=0,  # Устанавливаем первую вкладку по умолчанию
    )
    
    page.add(panel_exemples)

ft.app(target=main)
