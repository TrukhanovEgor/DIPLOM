import flet as ft

def exemples_breast(e, page):
    page.clean()

    app_bar = ft.AppBar(
        title=ft.Text("Грудные мышцы", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )
    

    # 1
    button1 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00251101-Barbell-Bench-Press_Chest-FIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Жим лежа",
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
        on_click=lambda e: exemples_breast(e, page),
    )

    # 2
    button2 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03141101-Dumbbell-Incline-Bench-Press_Chest_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Жим гантелей \n на наклонной \n скамье",
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
        on_click=lambda e: exemples_breast(e, page),
    )

    # 3
    button3 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F05961101-Lever-Seated-Fly_Chest_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Сведение рук  ",
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
        on_click=lambda e: exemples_breast(e, page),
    )

    # 4
    button4 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02891101-Dumbbell-Bench-Press_Chest_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Жим гантелей лежа",
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
        on_click=lambda e: exemples_breast(e, page),
    )

   # 5
    button5 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02271101-Cable-Standing-Fly_Chest-FIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Сведение рук \n в кроссовере",
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
        on_click=lambda e: exemples_breast(e, page),
    )

    # 6
    button6 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F06621101-Push-up-m_Chest-FIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Отжимания",
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
        on_click=lambda e: exemples_breast(e, page),
    )

    # 7
    button7 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00471101-Barbell-Incline-Bench-Press_Chest_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Жим штанги на \n наклонной \n скамье",
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
        on_click=lambda e: exemples_breast(e, page),
    )

    # 8
    button8 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02511101-Chest-Dip_Chest_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Отжимания на \n брусьях",
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
        on_click=lambda e: exemples_breast(e, page),
    )

    # 9
    button9 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F01791101-Cable-Low-Fly_Chest-FIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Тяга нижнего блока \n в кроссовере",
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
        on_click=lambda e: exemples_breast(e, page),
    )

    # 10
    button10 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03081101-Dumbbell-Fly_Chest-FIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Разведение рук \n лежа",
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
        on_click=lambda e: exemples_breast(e, page),
    )

    # Создаем контент для страницы
    content = ft.ListView(
        controls=[button1,button2,button3,button4,button5,button6,button7,button8,button9,button10],
        width=400,  # Ширина прокрутки
        height=400,  # Высота прокрутки
        spacing=10,  # Используем spacing вместо padding
    )

    page.add(app_bar)
    page.add(content)
    page.update()