import flet as ft
from database import save_workout

def plan_abs(page: ft.Page, content_area: ft.Column, go_back, username, go_to_journal):
    content_area.controls.clear()

    # Статический заголовок
    title_text = ft.Text(
        "План: Убрать живот",
        size=18,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER,
        font_family="Arial",
    )

    # Кнопка "Назад"
    back_button = ft.ElevatedButton(
        text="Назад",
        on_click=go_back,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.DEEP_ORANGE_300,
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=ft.padding.symmetric(horizontal=15, vertical=8),
        ),
    )

    # Кнопка "Начать План"
    def on_start_click(e):
        # Сохраняем "виртуальную тренировку" для отображения в журнале
        save_workout(
            username=username,
            workout_name="Убрать живот",
            exercise_name="План: Убрать живот",
            sets_count="-",
            reps_count="-",
            muscle_group="План",
            start_time=None,
            end_time=None,
            duration=None,
        )
        page.snack_bar = ft.SnackBar(ft.Text("План 'Убрать живот' добавлен в журнал"))
        page.snack_bar.open = True
        page.update()
        go_to_journal(e)

    start_button = ft.ElevatedButton(
        text="Начать План",
        on_click=on_start_click,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_400,
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=ft.padding.symmetric(horizontal=15, vertical=8),
        ),
    )

    # Функция для создания карточки (оставьте как в вашем коде) ...
    def create_card(title, description, img_url=None, icon=None, width=300, height=160):
        screen_width = page.window.width if page.window.width > 0 else 350
        scale = min(1.0, screen_width / 400)
        card_width = width * scale
        card_height = height * scale
        text_content = []
        if icon:
            text_content.append(ft.Icon(icon, color=ft.colors.DEEP_ORANGE_300, size=20 * scale))
        text_content.extend([
            ft.Text(
                title,
                size=14 * scale,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.WHITE,
                text_align=ft.TextAlign.CENTER,
                font_family="Arial",
                max_lines=2,
                overflow=ft.TextOverflow.ELLIPSIS,
            ),
            ft.Text(
                description,
                size=10 * scale,
                color=ft.colors.WHITE70,
                text_align=ft.TextAlign.LEFT,
                font_family="Arial",
                width=card_width - 20 * scale,
            ),
        ])
        stack_content = []
        if img_url:
            stack_content.append(
                ft.Image(
                    src=img_url,
                    width=card_width,
                    height=card_height,
                    fit=ft.ImageFit.COVER,
                    border_radius=12,
                    opacity=0.6,
                    error_content=ft.Text("Ошибка изображения", color=ft.colors.RED_400, size=10),
                )
            )
        stack_content.append(
            ft.Container(
                gradient=ft.LinearGradient(
                    colors=["#B3000000", ft.colors.TRANSPARENT],
                    begin=ft.alignment.bottom_center,
                    end=ft.alignment.top_center,
                ),
                width=card_width,
                height=card_height,
                border_radius=12,
            )
        )
        stack_content.append(
            ft.Column(
                text_content,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=6 * scale,
                expand=True,
            )
        )
        return ft.Container(
            content=ft.Stack(stack_content),
            padding=8 * scale,
            width=card_width,
            height=card_height,
            margin=ft.margin.all(6 * scale),
            border_radius=12,
            bgcolor=ft.colors.GREY_900,
            shadow=[
                ft.BoxShadow(
                    color="#66000000",
                    blur_radius=6 * scale,
                    offset=ft.Offset(0, 3 * scale),
                    spread_radius=1 * scale,
                )
            ],
        )

    # Контент плана тренировок (оставьте как у вас)
    cards = [
        # ... (ваш массив карточек, как в вашем примере)
        create_card(
            title="Введение",
            description="Этот 8-недельный план поможет убрать жир ...",
            icon=ft.icons.INFO_OUTLINE,
            width=300,
            height=200,
        ),
        # ... остальные карточки ...
    ]

    container_height = page.height - 100 if page.height else 600

    content_area.controls.append(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            [back_button, title_text, start_button],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=ft.padding.symmetric(horizontal=10, vertical=8),
                        bgcolor=ft.colors.GREY_800,
                        border_radius=8,
                    ),
                    ft.Column(
                        controls=[ft.Row([card], alignment=ft.MainAxisAlignment.CENTER) for card in cards],
                        spacing=8,
                        scroll=ft.ScrollMode.AUTO,
                        expand=True,
                    ),
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
            height=container_height,
            padding=ft.padding.symmetric(horizontal=8, vertical=5),
            expand=True,
        )
    )
    content_area.expand = True
    page.update()