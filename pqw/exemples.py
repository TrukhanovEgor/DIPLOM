import flet as ft
from exemples_pres.exempless_pres import exempless_pres
from exemples_pres.exemples_back import exemples_back
from exemples_pres.exemples_biceps import exemples_biceps
from exemples_pres.exemplts_triceps import exemples_triceps
from exemples_pres.exemples_breast import exemples_breast
from exemples_pres.exemples_Forearms import exemples_Forearms
from exemples_pres.exmples_Legs import exemples_Legs
from exemples_pres.exemples_Shoulders import exemples_Shoulders

def create_panel_exempless(page):
    def build_button(text, image_url, callback):
        return ft.ElevatedButton(
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.Image(
                            src=image_url,
                            width=50,
                            height=50,
                            border_radius=10,
                        ),
                        ft.Text(
                            text,
                            size=25,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.WHITE,
                        ),
                    ]
                ),
                padding=ft.padding.all(10),
                border_radius=10
            ),
            bgcolor=ft.colors.TRANSPARENT,
            on_click=callback
        )

    buttons = ft.Column(
        controls=[
            build_button("Мышцы \n пресса", "https://avatars.mds.yandex.net/i?id=f1738083272db4d9b1b3669a619aee53a2e739b7-12472308-images-thumbs&n=13", lambda e: exempless_pres(e, page)),
            build_button("Мышцы \n спины", "https://i.pinimg.com/originals/4a/39/53/4a3953009d67e7ca0e70566d2f37bbbd.jpg", lambda e: exemples_back(e, page)),
            build_button("Бицепс", "https://fgun.ru/uploads/aa8db3852112af73360fb910a0808d43.jpg", lambda e: exemples_biceps(e, page)),
            build_button("Трицепс", "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_663f1057e31cce12caa08312_663f163fb6611d716c0c57a8/scale_1200", lambda e: exemples_triceps(e, page)),
            build_button("Грудные \n мышцы", "https://avatars.mds.yandex.net/i?id=dd85a27d3bf79d4cbd9f007ff1de9366_l-12504436-images-thumbs&n=13", lambda e: exemples_breast(e, page)),
            build_button("Предплечья", "https://builderbody.ru/wp-content/uploads/2022/07/10-1.jpg", lambda e: exemples_Forearms(e, page)),
            build_button("Ноги", "https://record-fitness.pro/media/Editor/image.jpeg", lambda e: exemples_Legs(e, page)),
            build_button("Плечи", "https://fgun.ru/uploads/3d1b3d007364e047272bdea96dae8cb7.jpg", lambda e: exemples_Shoulders(e, page)),
        ],
        spacing=10
    )

    return ft.ListView(
        controls=[buttons],
        expand=True,
        spacing=10,
        padding=10
    )
