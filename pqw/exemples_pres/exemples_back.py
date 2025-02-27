import flet as ft

def exemples_back(e, page):
    page.clean()

    app_bar = ft.AppBar(
        title=ft.Text("Спина", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

    # 1
    button1 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://fitnessdoctor.ru/wa-data/public/shop/products/70/38/3870/images/126721/126721.750x0.png",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Подтягивания",
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
        on_click=lambda e: exemples_back(e, page),
    )

    #2 
    button2 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://i.pinimg.com/originals/20/e7/0d/20e70d0cb06f4ccbb0a8cde72a57a69b.jpg",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Становая тяга",
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
        on_click=lambda e: exemples_back(e, page),
    )

    #3
    button3 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://s3assets.skimble.com/assets/2268763/image_iphone.jpg",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Вертикальная \n тяга",
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
        on_click=lambda e: exemples_back(e, page),
    )

    #4
    button4 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://i.pinimg.com/originals/90/10/26/9010263284f98955fcf49bc24e0258fb.png",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Гребля тяга сидя",
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
        on_click=lambda e: exemples_back(e, page),
    )

    #5
    button5 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://s3.amazonaws.com/prod.skimble/assets/1419622/image_iphone.jpg",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Тяга гантели \n одной рукой в \n наклоне ",
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
        on_click=lambda e: exemples_back(e, page),
    )

    #6
    button6 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://s3.amazonaws.com/prod.skimble/assets/1856213/image_iphone.jpg",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Шраги со штангой ",
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
        on_click=lambda e: exemples_back(e, page),
    )
    
    #7
    button7 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6JcMZQOk2AwBGKq0kM4qH67gUPC4V7F4gforXYy6z8aa5a9nWuV85DAFpYNiDpDkOrskq31r4ahUZCAKbZsiqXair5W1KeQEtnUfo11OS5ojY1lKkAkxUXzSQviJbfhDqbk8RsTTzZgDb/s320-rw/dumbellshrugs1.pngom/prod.skimble/assets/1419622/image_iphone.jpg",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Шраги с гантелями",#https://billstarrr.blogspot.com/2018/03/dumbbell-shrugs-4-sets.html
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
        on_click=lambda e: exemples_back(e, page),
    )

    #8
    button8 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://i0.wp.com/www.muscleandfitness.com/wp-content/uploads/2014/02/6119_B.jpg?w=800&h=630&crop=1&quality=86&strip=all",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Гиперэкстензия",
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
        on_click=lambda e: exemples_back(e, page),
    )

    #9
    button9 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://tony.ru/assets/i/ai/4/7/7/i/3278992.jpg",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Тяга в  наклоне ",
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
        on_click=lambda e: exemples_back(e, page),
    )

    #10
    button10 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://www.sportiwno.ru/upload/exercises/6860412331.jpg",
                        width=50,
                        height=50,
                        border_radius=50,
                    ),
                    ft.Text(
                        "Подтягивания \n обратным хватом",
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
        on_click=lambda e: exemples_back(e, page),
    )






# Создаем контент для страницы
    content = ft.ListView(
        controls=[button1,button2, button3, button4,button5,button6,button7,button8,button9,button10],
        width=400,  # Ширина прокрутки
        height=400,  # Высота прокрутки
        spacing=10,  # Используем spacing вместо padding
    )

    page.add(app_bar)
    page.add(content)
    page.update()