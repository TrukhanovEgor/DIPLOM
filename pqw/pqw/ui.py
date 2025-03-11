import flet as ft
from Plan.exemples_plan import exemples_plan

training_names = []

def create_app_bar():
    return ft.AppBar(
        title=ft.Text(
            "Упражнения",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.WHITE,
            style="font-family: 'Arial';"
        ),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

def create_panel_plans(content_area, selected_plan):
    return ft.Column(
        [
            ft.Container(
                content=ft.CupertinoSlidingSegmentedButton(
                    selected_index=0,
                    thumb_color=ft.colors.DEEP_ORANGE_300,
                    on_change=lambda e: show_page(e.control.selected_index, content_area, e, content_area.page),
                    padding=ft.padding.symmetric(0, 10),
                    controls=[
                        ft.Text("Тренировки", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("Личные", size=20, weight=ft.FontWeight.BOLD),
                    ],
                ),
                padding=ft.padding.symmetric(0, 5),
            ),
            selected_plan,
            content_area
        ]
    )

def show_page(selected_index, content_area, e, page):
    content_area.controls.clear()

    if selected_index == 0:
        show_examples_plan(page, content_area)
    elif selected_index == 1:
        show_personal_content(page, content_area)

    content_area.update()

def show_examples_plan(page, content_area):
    exemples_plan(page, content_area)

def show_personal_content(page, content_area):
    personal_content = ft.Column(
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
                        on_click=lambda e: create_new_training(content_area),
                    ),
                ],
                alignment=ft.MainAxisAlignment.END,
                spacing=10,
            ),
        ]
    )

    for training_name in training_names:
        personal_content.controls.append(
            ft.TextButton(
                text=training_name,
                on_click=lambda e: show_page(0, content_area, e, page),
                style=ft.ButtonStyle(
                    color=ft.colors.DEEP_ORANGE_300,
                    shape=ft.RoundedRectangleBorder(radius=10),
                ),
            )
        )

    if not training_names:
        personal_content.controls.append(
            ft.Text("Создайте тренировку", size=16, color=ft.colors.GREY)
        )

    content_area.controls.append(personal_content)

def create_new_training(content_area):
    content_area.controls.clear()

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

    content_area.controls.append(
        ft.Column(
            [
                ft.Container(height=30),
                name_training,
                ft.Container(height=30),
                days_count,
                ft.Container(height=50),
                ft.Container(
                    alignment=ft.Alignment(0, 1),
                    content=ft.Column(
                        [
                            ft.ElevatedButton(
                                text="Сохранить",
                                on_click=lambda e: save_training(content_area, name_training, days_count),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=30),
                                    bgcolor=ft.colors.DEEP_ORANGE_300,
                                    color=ft.colors.WHITE,
                                ),
                                width=200,
                            ),
                            ft.ElevatedButton(
                                text="Отменить",
                                on_click=lambda e: cancel_training(content_area),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=30),
                                    bgcolor=ft.colors.DEEP_ORANGE_300,
                                    color=ft.colors.WHITE,
                                ),
                                width=200,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        )
    )

    content_area.update()

def save_training(content_area, name_training, days_count):
    training_name = name_training.value
    days = days_count.value

    if training_name and days:
        training_names.append(training_name)
        print(f"Тренировка сохранена! Название: {training_name}, Количество дней: {days}")

        content_area.controls.clear()
        show_page(1, content_area, None, None)
    else:
        content_area.controls.append(
            ft.Text("Пожалуйста, заполните все поля.", size=16, color=ft.colors.RED)
        )

    content_area.update()

def cancel_training(content_area):
    content_area.controls.clear()
    show_page(1, content_area, None, None)