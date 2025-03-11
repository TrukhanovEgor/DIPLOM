import flet as ft

def exemples_biceps(e, page):
    page.clean()

    

    app_bar = ft.AppBar(
        title=ft.Text("бицепс", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.DEEP_ORANGE_300,
    )

    # 1
    button1 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03121101-Dumbbell-Hammer-Curl-II_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Text(
                        "Подъемы",
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
        on_click=lambda e: exemples_biceps(e, page),
    )

    # 2
    button2 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00311101-Barbell-Curl_Upper-Arms-FIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,    
                    ),
                    ft.Text(
                        "Подъемы \n штанги стоя ",
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
        on_click=lambda e: exemples_biceps(e, page),
    )

    # 3
    button3 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00701101-Barbell-Preacher-Curl_Upper-Arms-AFIX_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,    
                    ),
                    ft.Text(
                        "Подъемы на бицепс \n на скамье Скотта",
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
        on_click=lambda e: exemples_biceps(e, page),
    )

    # 4
    button4 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02941101-Dumbbell-Biceps-Curl_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,    
                    ),
                    ft.Text(
                        "Молотки",
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
        on_click=lambda e: exemples_biceps(e, page),
    )

    # 5
    button5 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F09761101-Band-concentration-curl_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,    
                    ),
                    ft.Text(
                        "Концунтрированный \n подъем",
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
        on_click=lambda e: exemples_biceps(e, page),
    )

    # 6
    button6 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04471101-EZ-Barbell-Curl_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,    
                    ),
                    ft.Text(
                        "обратные подъемы",
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
        on_click=lambda e: exemples_biceps(e, page),
    )

    # 7
    button7 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F16071101-Cable-Biceps-Curl-(SZ-bar)_Upper-arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,    
                    ),
                    ft.Text(
                        "Сгибание бицепсов \n на блоках",
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
        on_click=lambda e: exemples_biceps(e, page),
    )

    # 8
    button8 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F16361101-Cable-Overhead-Curl_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,    
                    ),
                    ft.Text(
                        "Разводка на \n низком блоке",
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
        on_click=lambda e: exemples_biceps(e, page),
    )

    # 9
    button9 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03151101-Dumbbell-Incline-Biceps-Curl_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,    
                    ),
                    ft.Text(
                        "Подъем гантелей \n на бицепс на \n наклонной скамье",
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
        on_click=lambda e: exemples_biceps(e, page),
    )
 
# 10
    button10 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04471101-EZ-Barbell-Curl_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,    
                    ),
                    ft.Text(
                        "Подъем штанги \n с кривым грифом ",
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
        on_click=lambda e: exemples_biceps(e, page),
    )

    # 11
    button11 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04221101-Dumbbell-Standing-One-Arm-Curl-(over-incline-bench)_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,    
                    ),
                    ft.Text(
                        "Подъем гантелей \n на бицепс на \n  скамье",
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
        on_click=lambda e: exemples_biceps(e, page),
    )

    # 12
    button12 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F43571101-Band-Biceps-Curl-(VERSION-2)_Upper-Arms_small.png&w=640&q=100",
                        width=80,
                        height=80,
                        border_radius=50,
                        fit=ft.ImageFit.CONTAIN,    
                    ),
                    ft.Text(
                        "Сгибание рук \n с резинкой",
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
        on_click=lambda e: exemples_biceps(e, page),    
    )

 
         
   




# Создаем контент для страницы
    content = ft.ListView(
        controls=[button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12],
        width=400,  # Ширина прокрутки
        height=400,  # Высота прокрутки
        spacing=10,  # Используем spacing вместо padding
    )

    page.add(app_bar)
    page.add(content)
    page.update()