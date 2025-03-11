import flet as ft

def exemples_triceps(e, page):
    page.clean()

    app_bar = ft.AppBar(
        title=ft.Text("трицепс", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

    # 1
    button1 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02411101-Cable-Triceps-Pushdown-(V-bar-attachment)_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Тяга верхнего \n блока ",
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
        on_click=lambda e: exemples_triceps(e, page),
    )

    # 2
    button2 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00601101-Barbell-Lying-Triceps-Extension-Skull-Crusher_Triceps-SFIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),  
                    ft.Text(
                        "Французский жим",
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
        on_click=lambda e: exemples_triceps(e, page),
    )

    # 3
    button3 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F01941101-Cable-Overhead-Triceps-Extension-(rope-attachment)_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),  
                    ft.Text(
                        "Тяга нижнего блока \n из-за головы",
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
        on_click=lambda e: exemples_triceps(e, page),
    )

    # 4
    button4 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04301101-Dumbbell-Standing-Triceps-Extension_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),  
                    ft.Text(
                        "Разгибание рук \n с гантелью ",
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
        on_click=lambda e: exemples_triceps(e, page),
    )

    # 5
    button5 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00191101-Assisted-Triceps-Dip-(kneeling)_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),  
                    ft.Text(
                        "отжимание на брусьях",
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
        on_click=lambda e: exemples_triceps(e, page),
    )

    # 6
    button6 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00301101-Barbell-Close-Grip-Bench-Press_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),  
                    ft.Text(
                        "Жим узким хватом",
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
        on_click=lambda e: exemples_triceps(e, page),
    )

    # 7 
    button7 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F34431101-Dip-on-Floor-with-Chair_Chest_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),  
                    ft.Text(
                        "Трицепс на \n стуле",
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
        on_click=lambda e: exemples_triceps(e, page),
    )
    
    # 8
    button8 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F16091101-Cable-One-Arm-Side-Triceps-Pushdown_Upper-arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),  
                    ft.Text(
                        "Обратный жим \n одной рукой ",
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
        on_click=lambda e: exemples_triceps(e, page),
    )

    # 9
    button9 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02591101-Close-Grip-Push-up_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),  
                    ft.Text(
                        "Бриллиантовое \n отжимание",
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
        on_click=lambda e: exemples_triceps(e, page),
    )

    # 10
    button10 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04231101-Dumbbell-Standing-One-Arm-Extension_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),  
                    ft.Text(
                        "Разгибание \n одной рукой",
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
        on_click=lambda e: exemples_triceps(e, page),
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