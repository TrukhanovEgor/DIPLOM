import flet as ft
from exemples_pres.exempless_pres import exempless_pres
from exemples_pres.exemples_back import exemples_back

def create_panel_exempless(page):
    # Контейнер Пресс
    button1 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://avatars.mds.yandex.net/i?id=f1738083272db4d9b1b3669a619aee53a2e739b7-12472308-images-thumbs&n=13",
                        width=50,
                        height=50,
                        border_radius=10,
                    ),
                    ft.Text(
                        "Мышцы \n пресса",
                        size=25,
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
        on_click=lambda e: exempless_pres(e, page,),
    )

    # Контейнер Спина
    button2 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://i.pinimg.com/originals/4a/39/53/4a3953009d67e7ca0e70566d2f37bbbd.jpg",
                        width=50,
                        height=50,
                        border_radius=10,
                    ),
                    ft.Text(
                        "Мышцы \n спины",
                        size=25,
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
        on_click=lambda e: exemples_back(e, page,)  # Прозрачный фон
    )   

    #контейнер Бицепс
    button3 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://fgun.ru/uploads/aa8db3852112af73360fb910a0808d43.jpg",
                        width=50,
                        height=50,
                        border_radius=10,
                    ),
                    ft.Text(
                        "Бицепс",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT  # Прозрачный фон
    )

    #контейнер Трицепс
    button4 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_663f1057e31cce12caa08312_663f163fb6611d716c0c57a8/scale_1200",
                        width=50,
                        height=50,
                        border_radius=10,
                    ),
                    ft.Text(
                        "Трицепс",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT  # Прозрачный фон
    )

    #контейнер Грудные
    button5 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://avatars.mds.yandex.net/i?id=dd85a27d3bf79d4cbd9f007ff1de9366_l-12504436-images-thumbs&n=13",
                        width=50,
                        height=50,
                        border_radius=10,
                    ),
                    ft.Text(
                        "Грудные \n мышцы",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT  # Прозрачный фон
    )

     #контейнер предплечья
    button6 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://builderbody.ru/wp-content/uploads/2022/07/10-1.jpg",
                        width=50,
                        height=50,
                        border_radius=10,
                    ),
                    ft.Text(
                        "предплечья",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT  # Прозрачный фон
    )

     #контейнер ноги
    button7 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://record-fitness.pro/media/Editor/image.jpeg",
                        width=50,
                        height=50,
                        border_radius=10,
                    ),
                    ft.Text(
                        "ноги",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT  # Прозрачный фон
    )

         #контейнер плечи
    button8 = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src="https://fgun.ru/uploads/3d1b3d007364e047272bdea96dae8cb7.jpg",
                        width=50,
                        height=50,
                        border_radius=10,
                    ),
                    ft.Text(
                        "плечи",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                        style="font-family: 'Arial';",
                    ),
                ]
            ),
            padding=ft.padding.all(10),
            border_radius=10
        ),
        bgcolor=ft.colors.TRANSPARENT  # Прозрачный фон
    )

    return ft.ListView(
        controls=[button1, button2, button3, button4, button5, button6, button7, button8],
        width=400,  # Ширина прокрутки
        height=400,  # Высота прокрутки
        padding=ft.padding.all(10)
    )



