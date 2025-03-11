import flet as ft
from datetime import datetime

def Pres2(e, page):
    from exemples_pres.exempless_pres import exempless_pres  # Импортируем здесь
    page.clean()

    # Создаем кнопку "Назад"
    back_button = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        icon_color=ft.colors.WHITE,
        on_click=lambda _: exempless_pres(e, page),
    )

    # Создаем AppBar
    app_bar = ft.AppBar(
        leading=back_button,
        title=ft.Text("Подъем туловища на наклонной \n скамье", size=15, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
        center_title=True,
    )

    video_path = ft.VideoMedia("video/video_Pres//1764002.mp4")

    my_video = ft.Container(
        content=ft.Video(
            expand=True,
            fill_color=ft.colors.DEEP_ORANGE_300,
            playlist=[video_path],
            autoplay=True,
            playlist_mode=ft.PlaylistMode.LOOP,
            aspect_ratio=16 / 9,
            filter_quality="high",
            on_loaded=lambda e: print("Видео 1 загружено"),
        ),
        padding=ft.padding.all(10),
        bgcolor=ft.colors.GREY_900,
        border_radius=15,
    )

    muscles = ft.Container(
        content=ft.Text("Мышцы : Прямые и косые , мышцы живота", size=17, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
        padding=ft.padding.all(10),
        border_radius=15,
    )

    img1 = ft.Container(
        content=ft.Image(
            src="https://s3assets.skimble.com/assets/1423838/image_iphone.jpg",
            width=300,
            height=300,
            fit=ft.ImageFit.CONTAIN,
        ),
        padding=ft.padding.all(10),
        border_radius=15,
        bgcolor=ft.colors.GREY_900,
    )

    # Контейнер для ввода веса и повторов
    weight_input = ft.TextField(
        hint_text="Вес (кг)",
        width=100,
        border_color=ft.colors.DEEP_ORANGE_300,
        border_width=2,
        border_radius=10,
        text_size=16,
    )
    reps_input = ft.TextField(
        hint_text="Повторы",
        width=100,
        border_color=ft.colors.DEEP_ORANGE_300,
        border_width=2,
        border_radius=10,
        text_size=16,
    )
    weight_reps_container = ft.Container(
        content=ft.Row(
            controls=[
                weight_input,
                reps_input,
                ft.IconButton(
                    icon=ft.icons.ADD,
                    icon_color=ft.colors.DEEP_ORANGE_300,
                    on_click=lambda _: add_weight_reps_container(page, weight_input.value, reps_input.value),
                ),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=ft.padding.all(10),
        bgcolor=ft.colors.GREY_900,
        border_radius=15,
    )

    # Список для хранения новых контейнеров
    weight_reps_containers = []

    def add_weight_reps_container(page, weight, reps):
        # Получаем текущую дату без времени
        current_date = datetime.now().strftime("%Y-%m-%d")

        new_container = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(
                        value=f"Дата:\n{current_date}",
                        width=80,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.colors.WHITE,
                        size=12,
                    ),
                    ft.Text(
                        value=f"Вес (КГ):\n{weight}",
                        width=80,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.colors.WHITE,
                        size=12,
                    ),
                    ft.Text(
                        value=f"Повторы:\n{reps}",
                        width=80,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.colors.WHITE,
                        size=12,
                    ),
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.all(10),
            bgcolor=ft.colors.DEEP_ORANGE_300,
            border_radius=15,
        )

        weight_reps_containers.append(new_container)
        # Добавляем новый контейнер под первым контейнером
        content_column = page.controls[1].controls[0]
        content_column.controls.insert(content_column.controls.index(weight_reps_container) + 1, new_container)
        page.update()

    content = ft.ListView(
        expand=True,
        spacing=10,
        controls=[
            ft.Column(
                controls=[my_video, muscles, img1, weight_reps_container],
                spacing=20,
                alignment=ft.MainAxisAlignment.START,
            )
        ],
    )

    page.add(app_bar)
    page.add(content)
    page.update()
