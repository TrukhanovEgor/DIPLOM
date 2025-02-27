import flet as ft

def exempless_pres(e, page):
    page.clean()

    app_bar = ft.AppBar(
        title=ft.Text("Мышцы пресса", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

    button1 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://s3.amazonaws.com/prod.skimble/assets/833629/image_iphone.jpg",
                        width=50,
                        height=50, 
                        border_radius=50,
                    ),
                    ft.Text(
                        "Подъем туловища \n на наклонной \n скамье",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT,
        on_click=lambda e: exempless_pres(e, page),
    )

    button2 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://avatars.mds.yandex.net/i?id=5aaaa947bd1835caf58fa69dd751adce_l-5112218-images-thumbs&n=13", 
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Подъем ног из \n положения лежа",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT,
        on_click=lambda e: exempless_pres(e, page),
    )

     # Кнопка 3
    button3 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://example.com/image3.jpg",  # Замените на нужный URL
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Наклоны в \n стороны с \n гантелями",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT,
        on_click=lambda e: exempless_pres(e, page),
    )

     # Кнопка 4
    button4 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://manofmany.com/wp-content/uploads/2023/09/The-7-Minute-Workout-Proven-by-Science-Abdominal-Crunch.jpg",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Гранчи (подъемы \n туловища из \n положения лежа)",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT,
        on_click=lambda e: exempless_pres(e, page),
    )

         # Кнопка 5
    button5 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://avatars.mds.yandex.net/i?id=792da3853a4e91ae5770f1741e63c6d2b491bc4b-5885354-images-thumbs&n=13",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Подъемы туловища",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT,
        on_click=lambda e: exempless_pres(e, page),
    )

    # Кнопка 6
    button6 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://i.pinimg.com/736x/27/b1/2e/27b12e6783a657032a6eac219d17a15f.jpg",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Подъемы ног",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT,
        on_click=lambda e: exempless_pres(e, page),
    )

    # Кнопка 7
    button7 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://tehnoteca.ru/img/2231/2230168/bodytrain_sit_up_bench_9.jpg",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Подъемы ног\n из положения лежа \n на \n горизонтальной скамье",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT,
        on_click=lambda e: exempless_pres(e, page),
    )

    # Кнопка 8
    button8 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://i.pinimg.com/736x/e0/a7/b0/e0a7b0907582c7caaaed57acccc04fbe.jpg",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Подъемы ног\n к груди из \n положения лежа",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT,
        on_click=lambda e: exempless_pres(e, page),
    )

        # Кнопка 9
    button9 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://i.pinimg.com/236x/55/93/8b/55938b32177438f880bcac8e5b592314--a-relationship-reverse-crunches.jpg",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Подъемы бедер \n с поворотом",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT,
        on_click=lambda e: exempless_pres(e, page),
    )

            # Кнопка 10
    button10 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://avatars.mds.yandex.net/i?id=429e031bdd245999b12b2005534d1f4e_sr-4756765-images-thumbs&n=13",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Подъемы бедер \n с поворотом",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT,
        on_click=lambda e: exempless_pres(e, page),
    )

    # Создаем контент для страницы
    content = ft.ListView(
        controls=[button1, button2, button3, button4, button5, button6, button7, button8, button9, button10],
        width=400,  # Ширина прокрутки
        height=400,  # Высота прокрутки
        spacing=10,  # Используем spacing вместо padding
    )

    page.add(app_bar)
    page.add(content)
    page.update()
