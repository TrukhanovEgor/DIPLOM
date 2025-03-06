import flet as ft

def exemples_Shoulders(e, page):
    page.clean()

    app_bar = ft.AppBar(
                title=ft.Text("Плечи", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

    button1 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03341101-Dumbbell-Lateral-Raise_shoulder-AFIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Разгибание рук",
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
        on_click=lambda e: exemples_Shoulders(e, page),
    )

    button2 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04051101-Dumbbell-Seated-Shoulder-Press_Shoulders_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Жим гантелей",
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
        on_click=lambda e: exemples_Shoulders(e, page),
    )

    button3 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03101101-Dumbbell-Front-Raise_Shoulders_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Подъем гантелей перед собой",
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
        on_click=lambda e: exemples_Shoulders(e, page),
    )

    button4 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F11651101-Barbell-Standing-Military-Press-(without-rack)_Shoulders-FIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Жим штанги \n перед собой ",
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
        on_click=lambda e: exemples_Shoulders(e, page),
    )

    button5 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F07651101-Smith-Seated-Shoulder-Press_Shoulders_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Жим штанги \n в смите",
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
        on_click=lambda e: exemples_Shoulders(e, page),
    )

    button6 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03261101-Dumbbell-Incline-Rear-Lateral-Raise_Shoulders_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Разведение рук \n на наклонной \n скамье",
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
        on_click=lambda e: exemples_Shoulders(e, page),
    )




    content = ft.ListView(
        controls=[button1,button2,button3,button4,button5,button6],
        width=400,  # Ширина прокрутки
        height=400,  # Высота прокрутки
        spacing=10, 
    )

    page.add(app_bar)
    page.add(content)
    page.update()