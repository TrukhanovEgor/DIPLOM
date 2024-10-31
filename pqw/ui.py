import flet as ft

def create_app_bar():
    return ft.AppBar(
        title=ft.Text("Упражнения", size=30, weight=ft.FontWeight.BOLD,
                      color=ft.colors.WHITE, style="font-family: 'Arial';"),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

def create_panel_exemples():
    return ft.Row([ft.Text("Упражнения")])

def create_panel_plans(content_area, selected_plan):
    return ft.Column(
        [
            ft.Container(
                content=ft.CupertinoSlidingSegmentedButton(
                    selected_index=0,
                    thumb_color=ft.colors.DEEP_ORANGE_300,
                    on_change=lambda e: show_page(e.control.selected_index, content_area),
                    padding=ft.padding.symmetric(0, 10),
                    controls=[
                        ft.Text("Тренировки", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("Личные", size=20, weight=ft.FontWeight.BOLD),
                    ],
                ),
                padding=ft.padding.symmetric(0, 10),
            ),
            selected_plan,
            content_area
        ]
    )

def show_page(selected_index, content_area):
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
                                on_click=lambda e: create_new_training(content_area),# Переход на новую страницу
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                        spacing=10,
                    ),
                    ft.Text("Содержимое страницы Личные", size=20),
                    ft.Text("Здесь можно добавить больше информации о личных планах.", size=16),
                ]
            )
        )
    
    content_area.update()  # Обновляем content_area

def create_new_training(content_area):
    content_area.controls.clear()# Очищаем предыдущий контент
    
    content_area.controls.append(
    
        ft.Column(
            [
                ft.Container(
                    padding=ft.padding.symmetric(10, 10),
                    content=ft.Text("Название тренировки:", size=14, weight=ft.FontWeight.BOLD,
                                    color=ft.colors.WHITE, style="font-family: 'Arial';"),
                ),
                ft.Container(
                    padding=ft.padding.symmetric(10, 10),
                    content=ft.Text("Количество дней:", size=14, weight=ft.FontWeight.BOLD,
                                    color=ft.colors.WHITE, style="font-family: 'Arial';"),
                ),
                ft.Container(expand=True,bgcolor=ft.colors.DEEP_ORANGE_300),  # Заполнитель, чтобы отодвинуть кнопки вниз
                # Добавление двух овальных кнопок
                ft.Row(
                    [
                        ft.ElevatedButton(
                            text="Сохранить",
                            on_click=lambda e: save_training(content_area),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=30),  # Овальная форма
                                bgcolor=ft.colors.DEEP_ORANGE_300,
                                color=ft.colors.WHITE,
                            ),
                        ),
                        ft.ElevatedButton(
                            text="Отменить",
                            on_click=lambda e: cancel_training(content_area),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=30),  # Овальная форма
                                bgcolor=ft.colors.DEEP_ORANGE_300,
                                color=ft.colors.WHITE,
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,  # Выравнивание элементов в начале колонки
            expand=True,  # Позволяет колонне занимать всё доступное пространство
        )
    )
    
    content_area.update()  # Обновляем content_area



    content_area.controls.clear()  # Очищаем предыдущий контент
    
   

def save_training(content_area):
    # Логика сохранения тренировки
    print("Тренировка сохранена!")
    # Здесь можно добавить дополнительную логику после сохранения

def cancel_training(content_area):
    # Логика отмены создания тренировки
    print("Создание тренировки отменено.")
    show_page(1, content_area)
    # Здесь можно добавить дополнительную логику для возврата к предыдущему экрану

