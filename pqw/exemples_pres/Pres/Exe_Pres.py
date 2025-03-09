import flet as ft

def Pres1(e, page):
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


    video_path = ft.VideoMedia("video//02771201.mp4")

    my_video = ft.Container(
        content=ft.Video(
            expand=True,
            fill_color=ft.colors.DEEP_ORANGE_300,
            playlist=[video_path],
            autoplay=True,
            playlist_mode=ft.PlaylistMode.LOOP,
            aspect_ratio=16 / 9,
            filter_quality="high",
            on_loaded=lambda e: print("Видео  1 загружено"),
            
        ),
        padding=ft.padding.all(10),
        bgcolor=ft.colors.GREY_900,
        border_radius=15,
    )
    muscles = ft.Container(
        content=ft.Text("Мышцы : Прямые мышцы живота", size=17 , weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
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
    weight_reps_container = ft.Container(
        content=ft.Row(
            controls=[
                ft.TextField(hint_text="Вес (кг)", width=100),
                ft.TextField(hint_text="Повторы", width=100),
                ft.IconButton(
                    icon=ft.icons.ADD,
                    on_click=lambda _: add_weight_reps_container(page),
                ),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=ft.padding.all(10),
        bgcolor=ft.colors.GREY_900,
        border_radius=15,
    )

    # Список для хранения контейнеров с весом и повторами
    weight_reps_containers = []

    def add_weight_reps_container(page):
        new_container = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("Вес: 100 кг", size=16, color=ft.colors.WHITE),
                    ft.Text("Повторы: 80", size=16, color=ft.colors.WHITE),
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.all(10),
            bgcolor=ft.colors.GREY_900,
            border_radius=15,
        )
        weight_reps_containers.append(new_container)
        page.add(new_container)
        page.update()


    content = ft.ListView(
    expand=True,
    spacing=10,
    controls=[
        ft.Column(
            controls=[my_video,muscles, img1, weight_reps_container],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
        )
    ]
)
    page.add(app_bar)
    page.add(content)
    page.update()
