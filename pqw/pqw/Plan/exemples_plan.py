import flet as ft

def exemples_plan(page, content_area):
    if page is None:
        return

    # Очистка только content_area
    content_area.controls.clear()

    app_bar = ft.AppBar(
        title=ft.Text("Планы", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

    # Создаем первую кнопку
    button1 = ft.Container(
        content=ft.Column(
            [
                ft.Image(
                    src="https://www.lyfta.app/_next/image?url=https%3A%2F%2Flyfta.app%2Fimages%2Fexercises%2F37241101.png&w=640&q=10",
                    width=140,  # Ширина изображения
                    height=140,  # Высота изображения
                    fit=ft.ImageFit.CONTAIN,  # Изображение помещается в заданную область
                ),
                ft.Text(
                    "Фитнес клуб",
                    size=14,  # Размер текста
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=5,  # Отступы
        bgcolor=ft.colors.GREY_900,  # Белый фон
        border_radius=15,  # Радиус скругления углов
        width=150,
        height=180,
    )

    # Создаем вторую кнопку
    button2 = ft.Container(
        content=ft.Column(
            [
                ft.Image(
                    src="https://www.lyfta.app/_next/image?url=https%3A%2F%2Flyfta.app%2Fimages%2Fexercises%2F04651101.png&w=384&q=10",  # Замените на нужный URL
                    width=120,  # Ширина изображения
                    height=120,  # Высота изображения
                    fit=ft.ImageFit.CONTAIN,  # Изображение помещается в заданную область
                ),
                ft.Text(
                    "Комплекс для дома",
                    size=14,  # Размер текста
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=5,  # Отступы
        bgcolor=ft.colors.GREY_900,  # Белый фон
        border_radius=15,  # Радиус скругления углов
        width=150,
        height=180,
    )
    
    button3 = ft.Container(
        content=ft.Column(
            [
                ft.Image(
                    src="https://www.lyfta.app/_next/image?url=https%3A%2F%2Flyfta.app%2Fimages%2Fexercises%2F06521101.png&w=384&q=10",  # Замените на нужный URL
                    width=150,  # Ширина изображения
                    height=110,  # Высота изображения
                    fit=ft.ImageFit.CONTAIN,  # Изображение помещается в заданную область
                ),
                ft.Text(
                    "Домашний спортзал",
                    size=14,  # Размер текста
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=5,  # Отступы
        bgcolor=ft.colors.GREY_900,  # Белый фон
        border_radius=15,  # Радиус скругления углов
        width=300,
        height=150,
    )

    button4 = ft.Container(
        content=ft.Column(
            [
                ft.Image(
                    src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02391101-Cable-Straight-Back-Seated-Row_Back_small.png&w=640&q=100",  # Замените на нужный URL
                    width=120,  # Ширина изображения
                    height=120,  # Высота изображения
                    fit=ft.ImageFit.CONTAIN,  # Изображение помещается в заданную область
                ),
                ft.Text(
                    "Жим и Тяги",
                    size=14,  # Размер текста
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=5,  # Отступы
        bgcolor=ft.colors.GREY_900,  # Белый фон
        border_radius=15,  # Радиус скругления углов
        width=150,
        height=180,
    )

    button5 = ft.Container(
        content=ft.Column(
            [
                ft.Image(
                    src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F45111101-Bridge-Pose-Setu-Bandhasana-(male)_Stretching_small.png&w=640&q=100",  # Замените на нужный URL
                    width=120,  # Ширина изображения
                    height=120,  # Высота изображения
                    fit=ft.ImageFit.CONTAIN,  # Изображение помещается в заданную область
                ),
                ft.Text(
                    "Стройное тело",
                    size=14,  # Размер текста
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=5,  # Отступы
        bgcolor=ft.colors.GREY_900,  # Белый фон
        border_radius=15,  # Радиус скругления углов
        width=150,
        height=180,
    )

    button6 = ft.Container(
        content=ft.Column(
            [
                ft.Image(
                    src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02741101-Crunch-Floor-m_waist_small.png&w=640&q=100",  # Замените на нужный URL
                    width=150,  # Ширина изображения
                    height=110,  # Высота изображения
                    fit=ft.ImageFit.CONTAIN,  # Изображение помещается в заданную область
                ),
                ft.Text(
                    "Рефленый пресс",
                    size=14,  # Размер текста
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=5,  # Отступы
        bgcolor=ft.colors.GREY_900,  # Белый фон
        border_radius=15,  # Радиус скругления углов
        width=300,
        height=150,
    )
    
    button7 = ft.Container(
        content=ft.Column(
            [
                ft.Image(
                    src="*",  # Замените на нужный URL
                    width=150,  # Ширина изображения
                    height=110,  # Высота изображения
                    fit=ft.ImageFit.CONTAIN,  # Изображение помещается в заданную область
                ),
                ft.Text(
                    "",
                    size=14,  # Размер текста
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=5,  # Отступы
        bgcolor=ft.colors.TRANSPARENT,  # Белый фон
        border_radius=15,  # Радиус скругления углов
        width=300,
        height=100,
    )



    # Размещаем кнопки в одном ряду
    buttons_row = ft.Row(
        controls=[button1, button2],
        spacing=15,  # Расстояние между кнопками
        alignment=ft.MainAxisAlignment.CENTER,  # Центрирование по горизонтали
    )

    buttons_row2 = ft.Row(
        controls=[button4, button5 ],
        spacing=15,  # Расстояние между кнопками
        alignment=ft.MainAxisAlignment.CENTER,  # Центрирование по горизонтали
    )

    content = ft.ListView(
        controls=[buttons_row, button3,buttons_row2,button6,button7],
        width=400,
        height=400,
        spacing=10,
    )

    page.add(app_bar)
    content_area.controls.append(content)
    page.update()
