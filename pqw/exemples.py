import flet as ft
from exemples_pres.exempless_pres import exempless_pres
from exemples_pres.exemples_back import exemples_back
from exemples_pres.exemples_biceps import exemples_biceps
from exemples_pres.exemplts_triceps import exemples_triceps
from exemples_pres.exemples_breast import exemples_breast
from exemples_pres.exemples_Forearms import exemples_Forearms
from exemples_pres.exmples_Legs import exemples_Legs
from exemples_pres.exemples_Shoulders import exemples_Shoulders

MUSCLE_GROUPS = [
    {
        "title": "Мышцы пресса",
        "img": "https://avatars.mds.yandex.net/i?id=f1738083272db4d9b1b3669a619aee53a2e739b7-12472308-images-thumbs&n=13",
        "callback": exempless_pres
    },
    {
        "title": "Мышцы спины",
        "img": "https://i.pinimg.com/originals/4a/39/53/4a3953009d67e7ca0e70566d2f37bbbd.jpg",
        "callback": exemples_back
    },
    {
        "title": "Бицепс",
        "img": "https://fgun.ru/uploads/aa8db3852112af73360fb910a0808d43.jpg",
        "callback": exemples_biceps
    },
    {
        "title": "Трицепс",
        "img": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_663f1057e31cce12caa08312_663f163fb6611d716c0c57a8/scale_1200",
        "callback": exemples_triceps
    },
    {
        "title": "Грудные мышцы",
        "img": "https://avatars.mds.yandex.net/i?id=dd85a27d3bf79d4cbd9f007ff1de9366_l-12504436-images-thumbs&n=13",
        "callback": exemples_breast
    },
    {
        "title": "Предплечья",
        "img": "https://builderbody.ru/wp-content/uploads/2022/07/10-1.jpg",
        "callback": exemples_Forearms
    },
    {
        "title": "Ноги",
        "img": "https://record-fitness.pro/media/Editor/image.jpeg",
        "callback": exemples_Legs
    },
    {
        "title": "Плечи",
        "img": "https://fgun.ru/uploads/3d1b3d007364e047272bdea96dae8cb7.jpg",
        "callback": exemples_Shoulders
    },
]

def muscle_tile(title, image_url, callback, page):
    card = ft.Container(
        content=ft.Row(
            [
                ft.Image(
                    src=image_url,
                    width=64,
                    height=64,
                    border_radius=16,
                    fit=ft.ImageFit.COVER
                ),
                ft.Container(width=10),
                ft.Text(
                    title,
                    size=19,
                    weight=ft.FontWeight.W_700,
                    color=ft.colors.WHITE,
                    max_lines=2,
                    overflow=ft.TextOverflow.ELLIPSIS
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=14,
        border_radius=18,
        bgcolor=ft.colors.with_opacity(0.2, ft.colors.BLUE_GREY_900),
        shadow=ft.BoxShadow(
            blur_radius=10,
            color=ft.colors.with_opacity(0.25, ft.colors.BLACK),
            spread_radius=1,
            offset=ft.Offset(0, 4)
        ),
        ink=True,
        animate=ft.animation.Animation(200, "easeIn"),
        margin=ft.margin.all(4),
        on_click=lambda e: callback(e, page),
    )
    # Курсор "рука" только через GestureDetector:
    return ft.GestureDetector(
        content=card,
        mouse_cursor=ft.MouseCursor.CLICK,
        on_tap=lambda e: callback(e, page)
    )

def create_panel_exempless(page):
    grid = ft.GridView(
        runs_count=2,
        max_extent=340,
        child_aspect_ratio=2.7,
        spacing=10,
        run_spacing=10,
        padding=ft.padding.symmetric(horizontal=12, vertical=16),
        expand=True,
        controls=[
            muscle_tile(m["title"], m["img"], m["callback"], page)
            for m in MUSCLE_GROUPS
        ]
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Выберите группу мышц", 
                    size=26, 
                    weight=ft.FontWeight.BOLD, 
                    color=ft.colors.CYAN_200,
                    text_align=ft.TextAlign.CENTER,
                ),
                grid
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=10
        ),
        expand=True,
        bgcolor="#0e1621"
    )