import flet as ft
from Plan.plan_fitness_club import plan_fitness_club
from Plan.plan_home import plan_home
from Plan.plan_gym import plan_gym
from Plan.plan_push_pull import plan_push_pull
from Plan.plan_body_shape import plan_body_shape
from Plan.plan_abs import plan_abs

def exemples_plan(page: ft.Page, content: ft.Column):
    content.controls.clear()

    title_text = ft.Text(
        "Выберите ваш план",
        size=22,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER,
        font_family="Arial",
    )

    def open_plan(plan_func, plan_name):
        def handler(e):
            content.controls.clear()
            page.snack_bar = ft.SnackBar(ft.Text(f"Открытие плана: {plan_name}"))
            page.snack_bar.open = True
            def go_back(e):
                exemples_plan(page, content)
            plan_func(page, content, go_back)
            page.update()
        return handler

    def create_plan_card(img_url, title, description, handler, location, width=150, height=200, is_wide=False):
        return ft.Container(
            content=ft.Stack(
                [
                    ft.Image(
                        src=img_url,
                        width=width,
                        height=height,
                        fit=ft.ImageFit.COVER,
                        border_radius=12,
                        opacity=0.6,
                        error_content=ft.Text("Ошибка изображения", color=ft.colors.RED_400, size=12),
                    ),
                    ft.Container(
                        gradient=ft.LinearGradient(
                            colors=["#B3000000", ft.colors.TRANSPARENT],
                            begin=ft.alignment.bottom_center,
                            end=ft.alignment.top_center,
                        ),
                        width=width,
                        height=height,
                        border_radius=12,
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                title,
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                                font_family="Arial",
                                max_lines=2,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            ft.Text(
                                location,
                                size=12,
                                color=ft.colors.DEEP_ORANGE_300,
                                text_align=ft.TextAlign.CENTER,
                                font_family="Arial",
                            ),
                            ft.Text(
                                description,
                                size=12,
                                color=ft.colors.WHITE70,
                                text_align=ft.TextAlign.CENTER,
                                max_lines=2,
                                overflow=ft.TextOverflow.ELLIPSIS,
                                font_family="Arial",
                            ),
                            ft.ElevatedButton(
                                text="Открыть",
                                on_click=handler,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.DEEP_ORANGE_300,
                                    color=ft.colors.WHITE,
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                    padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                ),
                                width=120,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=8,
                        expand=True,
                    ),
                ],
            ),
            padding=10,
            width=width,
            height=height,
            margin=ft.margin.all(8),
            border_radius=12,
            bgcolor=ft.colors.GREY_900,
            shadow=[
                ft.BoxShadow(
                    color="#66000000",
                    blur_radius=8,
                    offset=ft.Offset(0, 4),
                    spread_radius=1,
                )
            ],
        )

    plans = [
        {
            "title": "Убрать живот",
            "description": "Сжигание жира и укрепление кора.",
            "img_url": "https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02741101-Crunch-Floor-m_waist_small.png&w=640&q=100",
            "handler": open_plan(plan_abs, "Убрать живот"),
            "location": "Для дома",
            "width": 150,
            "height": 200,
            "is_wide": False,
        },
        {
            "title": "Набрать мышцы",
            "description": "Силовые тренировки для роста мышц.",
            "img_url": "https://www.lyfta.app/_next/image?url=https%3A%2F%2Flyfta.app%2Fimages%2Fexercises%2F37241101.png&w=640&q=10",
            "handler": open_plan(plan_fitness_club, "Набрать мышцы"),
            "location": "Для спортзала",
            "width": 150,
            "height": 200,
            "is_wide": False,
        },
        {
            "title": "Рельефный пресс",
            "description": "Чёткий рельеф пресса за 8 недель.",
            "img_url": "https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02741101-Crunch-Floor-m_waist_small.png&w=640&q=100",
            "handler": open_plan(plan_abs, "Рельефный пресс"),
            "location": "Для дома",
            "width": 320,
            "height": 180,
            "is_wide": True,
        },
        {
            "title": "Силовая выносливость",
            "description": "Сила и выносливость для интенсивных тренировок.",
            "img_url": "https://www.lyfta.app/_next/image?url=https%3A%2F%2Flyfta.app%2Fimages%2Fexercises%2F06521101.png&w=384&q=10",
            "handler": open_plan(plan_gym, "Силовая выносливость"),
            "location": "Для спортзала",
            "width": 150,
            "height": 200,
            "is_wide": False,
        },
        {
            "title": "Гибкость и растяжка",
            "description": "Улучшение гибкости и восстановление.",
            "img_url": "https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F45111101-Bridge-Pose-Setu-Bandhasana-(male)_Stretching_small.png&w=640&q=100",
            "handler": open_plan(plan_body_shape, "Гибкость и растяжка"),
            "location": "Для дома",
            "width": 150,
            "height": 200,
            "is_wide": False,
        },
        {
            "title": "Жим и тяги",
            "description": "Силовые упражнения для верха тела.",
            "img_url": "https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02391101-Cable-Straight-Back-Seated-Row_Back_small.png&w=640&q=100",
            "handler": open_plan(plan_push_pull, "Жим и тяги"),
            "location": "Для спортзала",
            "width": 320,
            "height": 180,
            "is_wide": True,
        },
    ]

    # Создаём строки для карточек без горизонтальной прокрутки
    rows = []
    i = 0
    while i < len(plans):
        if not plans[i]["is_wide"] and i + 1 < len(plans) and not plans[i + 1]["is_wide"]:
            rows.append(
                ft.Row(
                    controls=[
                        create_plan_card(**plans[i]),
                        create_plan_card(**plans[i + 1]),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                )
            )
            i += 2
        else:
            rows.append(
                ft.Row(
                    controls=[
                        create_plan_card(**plans[i]),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                )
            )
            i += 1

    # Создаём контейнер с вертикальной прокруткой
    content.controls.append(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=title_text,
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(top=15, bottom=10),
                    ),
                    *rows,
                ],
                spacing=10,
                scroll=ft.ScrollMode.AUTO,  # Включаем вертикальный скролл
                expand=True,
            ),
            height=page.height - 80,  # Ограничиваем высоту
            padding=ft.padding.symmetric(horizontal=10),
            expand=True,
        )
    )

    # Устанавливаем параметры для content
    content.scroll = ft.ScrollMode.AUTO
    content.expand = True
    page.update()

if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Тренировочные планы"
        page.bgcolor = ft.colors.BLACK
        content_area = ft.Column(expand=True)
        page.add(
            ft.Container(
                content=content_area,
                expand=True,
                padding=ft.padding.all(10),
                height=page.height,  # Ограничиваем высоту страницы
            )
        )
        exemples_plan(page, content_area)
    ft.app(target=main)


