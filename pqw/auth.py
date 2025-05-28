import flet as ft
from database import register_user, login_user, user_exists

def auth_page(page, on_login_success):
    username_field = ft.TextField(
        label="Имя пользователя",
        width=320,
        border_radius=12,
        filled=True,
        prefix_icon=ft.icons.PERSON
    )
    password_field = ft.TextField(
        label="Пароль",
        password=True,
        can_reveal_password=True,
        width=320,
        border_radius=12,
        filled=True,
        prefix_icon=ft.icons.LOCK
    )

    message = ft.Text("", size=14, color=ft.colors.ERROR)
    mode = {"register": False}

    def switch_mode(e):
        mode["register"] = not mode["register"]
        username_field.value = ""
        password_field.value = ""
        message.value = ""
        update_labels()
        page.update()

    title = ft.Text(
        "Вход",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.ON_SURFACE
    )
    action_button = ft.ElevatedButton(
        "Войти",
        width=220,
        on_click=lambda e: handle_action(e),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            bgcolor=ft.colors.PRIMARY,
            color=ft.colors.ON_PRIMARY,
            overlay_color=ft.colors.PRIMARY_CONTAINER
        )
    )
    switch_button = ft.TextButton(
        "Зарегистрироваться",
        icon=ft.icons.PERSON_ADD,
        on_click=switch_mode,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            color=ft.colors.PRIMARY,
        )
    )

    def update_labels():
        if mode["register"]:
            title.value = "Регистрация"
            action_button.text = "Зарегистрироваться"
            switch_button.text = "Войти"
            switch_button.icon = ft.icons.LOGIN
        else:
            title.value = "Вход"
            action_button.text = "Войти"
            switch_button.text = "Зарегистрироваться"
            switch_button.icon = ft.icons.PERSON_ADD

    def handle_action(e):
        username = username_field.value.strip()
        password = password_field.value.strip()

        if not username or not password:
            message.value = "Поля не могут быть пустыми."
            message.color = ft.colors.ERROR
        elif mode["register"]:
            if user_exists(username):
                message.value = "Пользователь с таким именем уже существует."
                message.color = ft.colors.ERROR
            else:
                register_user(username, password)
                message.value = "Регистрация успешна. Войдите."
                message.color = ft.colors.GREEN
                switch_mode(None)
        else:
            if not user_exists(username):
                message.value = "Такой пользователь не зарегистрирован."
                message.color = ft.colors.ERROR
            elif login_user(username, password):
                message.value = "Успешный вход!"
                message.color = ft.colors.GREEN
                page.update()
                on_login_success(username)
                return
            else:
                message.value = "Неверный пароль."
                message.color = ft.colors.ERROR

        page.update()

    # Card with elevation and rounded corners for modern look
    form_card = ft.Container(
        content=ft.Column(
            [
                ft.Row([ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=56, color=ft.colors.PRIMARY)], alignment=ft.MainAxisAlignment.CENTER),
                title,
                username_field,
                password_field,
                message,
                action_button,
                switch_button
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=40,
        border_radius=18,
        bgcolor="rgba(255,255,255,0.97)",  # <-- ПРОЗРАЧНОСТЬ ЧЕРЕЗ RGBA
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=18,
            color="rgba(25, 118, 210, 0.1)",  # PRIMARY как rgba
            offset=ft.Offset(0, 6)
        ),
        width=400,
        margin=ft.margin.only(top=60, bottom=60)
    )

    # Gradient background
    return ft.Stack(
        [
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[ft.colors.BLUE_100, ft.colors.INDIGO_100, ft.colors.WHITE]
                ),
            ),
            ft.Row(
                [form_card],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
        ]
    )