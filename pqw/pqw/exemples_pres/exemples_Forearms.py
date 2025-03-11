import flet as ft

def exemples_Forearms(e, page):
    page.clean()

    app_bar = ft.AppBar(
                title=ft.Text("Предплечье", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

    button1 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F01251101-Barbell-Wrist-Curl-II_Forearms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Сгибание/ \n разгибание \n зяпястий",
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
        on_click=lambda e: exemples_Forearms(e, page),
    )

    button2 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F01251101-Barbell-Wrist-Curl-II_Forearms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Сгибание/ \n разгибание \n зяпястий",
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
        on_click=lambda e: exemples_Forearms(e, page),
    )

    button3 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F70561101-Dumbbell-Standing-Reverse-Curl-Rotate-(male)_Forearms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Повороты рук \n с гантелями",
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
        on_click=lambda e: exemples_Forearms(e, page),
    )

    button4 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03691101-Dumbbell-Over-Bench-Wrist-Curl_Forearms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Скручивание рук \n с гантелями",
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
        on_click=lambda e: exemples_Forearms(e, page),
    )




    content = ft.ListView(
        controls=[button1,button2,button3,button4],
        width=400,  # Ширина прокрутки
        height=400,  # Высота прокрутки
        spacing=10, 
    )

    page.add(app_bar)
    page.add(content)
    page.update()