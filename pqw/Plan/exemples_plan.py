import flet as ft
from Plan.plan_fitness_club import plan_fitness_club
from Plan.plan_home import plan_home
from Plan.plan_gym import plan_gym
from Plan.plan_push_pull import plan_push_pull
from Plan.plan_body_shape import plan_body_shape
from Plan.plan_abs import plan_abs

def exemples_plan(page, content_area):
    if page is None:
        return

    def open_plan(plan_func):
        def handler(e):
            content_area.controls.clear()
            plan_func(page, content_area)
            page.update()
        return handler

    content_area.controls.clear()

    app_bar = ft.AppBar(
        title=ft.Text("Планы", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

    def create_button(img_url, text, handler, width=150, height=180):
        return ft.GestureDetector(
            on_tap=handler,
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Image(src=img_url, width=120, height=120, fit=ft.ImageFit.CONTAIN),
                        ft.Text(text, size=14, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=5,
                bgcolor=ft.colors.GREY_900,
                border_radius=15,
                width=width,
                height=height,
            )
        )

    buttons = [
        create_button(
            "https://www.lyfta.app/_next/image?url=https%3A%2F%2Flyfta.app%2Fimages%2Fexercises%2F37241101.png&w=640&q=10",
            "Фитнес клуб", open_plan(plan_fitness_club)
        ),
        create_button(
            "https://www.lyfta.app/_next/image?url=https%3A%2F%2Flyfta.app%2Fimages%2Fexercises%2F04651101.png&w=384&q=10",
            "Комплекс для дома", open_plan(plan_home)
        ),
        create_button(
            "https://www.lyfta.app/_next/image?url=https%3A%2F%2Flyfta.app%2Fimages%2Fexercises%2F06521101.png&w=384&q=10",
            "Домашний спортзал", open_plan(plan_gym), width=300, height=150
        ),
        create_button(
            "https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02391101-Cable-Straight-Back-Seated-Row_Back_small.png&w=640&q=100",
            "Жим и Тяги", open_plan(plan_push_pull)
        ),
        create_button(
            "https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F45111101-Bridge-Pose-Setu-Bandhasana-(male)_Stretching_small.png&w=640&q=100",
            "Стройное тело", open_plan(plan_body_shape)
        ),
        create_button(
            "https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02741101-Crunch-Floor-m_waist_small.png&w=640&q=100",
            "Рельефный пресс", open_plan(plan_abs), width=300, height=150
        ),
    ]

    rows = [ft.Row(controls=buttons[i:i+2], spacing=15, alignment=ft.MainAxisAlignment.CENTER) for i in range(0, len(buttons), 2)]

    content = ft.ListView(
        controls=rows,
        width=400,
        height=400,
        spacing=10,
    )



    page.add(app_bar)
    content_area.controls.append(content)
