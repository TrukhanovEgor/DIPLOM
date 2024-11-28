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
    content_area.controls.clear()  # Очищаем предыдущий контент
    
    # Создаем текстовые поля
    name_training = ft.TextField(
        label="Название тренировки",
        width=200,
        height=40,
        text_size=20,
        autofocus=True
    )
    
    days_count = ft.TextField(
        label="Количество дней",
        width=200,
        height=40,
        text_size=20,
        autofocus=True
    )
    
    # Добавляем текстовые поля и кнопки в content_area
    content_area.controls.append(
        ft.Column(
            [
                ft.Container(height=30),
                name_training,
                ft.Container(height=30),
                days_count,
                ft.Container(height=50),  # Отступ между полями и кнопками
                
                ft.Container(
                    alignment=ft.Alignment(0, 1),  # Центрирование по горизонтали
                    content=ft.Column(
                        [
                            ft.ElevatedButton(
                                text="Сохранить",
                                on_click=lambda e: save_training(content_area, name_training, days_count),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=30),  # Овальная форма
                                    bgcolor=ft.colors.DEEP_ORANGE_300,
                                    color=ft.colors.WHITE,
                                ),
                                width=200,  # Ширина кнопки                           
                            ),
                            ft.ElevatedButton(
                                text="Отменить",
                                on_click=lambda e: cancel_training(content_area),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=30),  # Овальная форма
                                    bgcolor=ft.colors.DEEP_ORANGE_300,
                                    color=ft.colors.WHITE,
                                ),
                                width=200,  # Ширина кнопки   
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,  # Выравнивание элементов в начале колонки
            expand=True,  # Позволяет колонне занимать всё доступное пространство
        )
    )

    content_area.update()  # Обновляем content_area

def save_training(content_area, name_training, days_count):
    # Получаем значения из текстовых полей
    training_name = name_training.value
    days = days_count.value
    
    # Логика сохранения тренировки
    print(f"Тренировка сохранена! Название: {training_name}, Количество дней: {days}")
    
    # Здесь можно добавить дополнительную логику для сохранения данных в базу данных или файл

    # Возвращаемся на предыдущую страницу или показываем сообщение об успешном сохранении
    show_page(1, content_area)
def cancel_training(content_area):
    # Логика отмены создания тренировки
    print("Создание тренировки отменено.")
    show_page(1, content_area)
    # Здесь можно добавить дополнительную логику для возврата к предыдущему экрану

