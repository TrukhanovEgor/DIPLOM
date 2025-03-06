import flet as ft

def exemples_Legs(e, page):
    page.clean()

    app_bar = ft.AppBar(
                title=ft.Text("Ноги", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

    button1 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F05851101-Lever-Leg-Extension_Thighs_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Разгибание ног",
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
        on_click=lambda e: exemples_Legs(e, page),
    )

    button2 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00431101-Barbell-Full-Squat_Thighs_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Приседание",
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
        on_click=lambda e: exemples_Legs(e, page),
    )

    button3 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F05991101-Lever-Seated-Leg-Curl_Thighs-FIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Сгибание ног",
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
        on_click=lambda e: exemples_Legs(e, page),
    )

    button4 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F07401101-Sled-45-Leg-Wide-Press_Thighs_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Жим ногами \n под углом",
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
        on_click=lambda e: exemples_Legs(e, page),
    )

    button5 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F22901101-Dumbbell-Bulgarian-Split-Squat-(female)_Thighs_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Выподы с гантелями",
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
        on_click=lambda e: exemples_Legs(e, page),
    )

    button6 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F05981101-Lever-Seated-Hip-Adduction_Thighs_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Сведение ног \n в тренажоре",
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
        on_click=lambda e: exemples_Legs(e, page),
    )

    button7 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F17601101-Dumbbell-Goblet-Squat_Thighs-FIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Приседание с \n гантелями",
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
        on_click=lambda e: exemples_Legs(e, page),
    )

    button8 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F07411101-Sled-Closer-Hack-Squat_Thighs_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Приседание в \n тренажоре",
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
        on_click=lambda e: exemples_Legs(e, page),
    )

    button9 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F31931101-Glute-Ham-Raise_Thighs-FIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Гиперэкстензия ",
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
        on_click=lambda e: exemples_Legs(e, page),
    )

    button10 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F24781101-Barbell-Lunge-(female)_Thighs_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Выподы со штангой",
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
        on_click=lambda e: exemples_Legs(e, page),
    )










    content = ft.ListView(
        controls=[button1, button2, button3, button4, button5, button6, button7, button8, button9, button10],
        width=400,  # Ширина прокрутки
        height=400,  # Высота прокрутки
        spacing=10, 
    )

    page.add(app_bar)
    page.add(content)
    page.update()