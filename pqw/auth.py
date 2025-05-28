import flet as ft
from database import register_user, login_user, user_exists

def auth_page(page, on_login_success):
    username_field = ft.TextField(
        label="Имя пользователя",
        width=320,
        border_radius=12,
        filled=True,
        prefix_icon=ft.icons.PERSON,
    )
    password_field = ft.TextField(
        label="Пароль",
        password=True,
        can_reveal_password=True,
        width=320,
        border_radius=12,
        filled=True,
        prefix_icon=ft.icons.LOCK,
    )
    password_repeat_field = ft.TextField(
        label="Повторите пароль",
        password=True,
        can_reveal_password=True,
        width=320,
        border_radius=12,
        filled=True,
        prefix_icon=ft.icons.LOCK_OUTLINE,
        visible=False,
    )

    message = ft.Text("", size=14, color=ft.colors.ERROR)
    mode = {"register": False}

    def set_register_mode(register: bool):
        mode["register"] = register
        username_field.value = ""
        password_field.value = ""
        password_repeat_field.value = ""
        message.value = ""
        password_repeat_field.visible = register
        update_labels()
        page.update()

    def switch_mode(e):
        set_register_mode(not mode["register"])

    title = ft.Text(
        "Вход",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.ON_SURFACE,
    )
    action_button = ft.ElevatedButton(
        "Войти",
        width=220,
        on_click=lambda e: handle_action(e),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            bgcolor=ft.colors.PRIMARY,
            color=ft.colors.ON_PRIMARY,
            overlay_color=ft.colors.PRIMARY_CONTAINER,
        ),
    )
    switch_button = ft.TextButton(
        "Зарегистрироваться",
        icon=ft.icons.PERSON_ADD,
        on_click=switch_mode,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            color=ft.colors.PRIMARY,
        ),
    )

    def update_labels():
        if mode["register"]:
            title.value = "Регистрация"
            action_button.text = "Зарегистрироваться"
            switch_button.text = "Войти"
            switch_button.icon = ft.icons.LOGIN
            password_repeat_field.visible = True
        else:
            title.value = "Вход"
            action_button.text = "Войти"
            switch_button.text = "Зарегистрироваться"
            switch_button.icon = ft.icons.PERSON_ADD
            password_repeat_field.visible = False

    def handle_action(e):
        username = username_field.value.strip()
        password = password_field.value.strip()
        password_repeat = password_repeat_field.value.strip()

        if not username or not password or (mode["register"] and not password_repeat):
            message.value = "Все поля должны быть заполнены."
            message.color = ft.colors.ERROR
        elif mode["register"]:
            if user_exists(username):
                message.value = "Пользователь с таким именем уже существует."
                message.color = ft.colors.ERROR
            elif password != password_repeat:
                message.value = "Пароли не совпадают."
                message.color = ft.colors.ERROR
            elif len(password) < 6:
                message.value = "Пароль должен содержать не менее 6 символов."
                message.color = ft.colors.ERROR
            elif not any(c.isdigit() for c in password) or not any(c.isalpha() for c in password):
                message.value = "Пароль должен содержать буквы и цифры."
                message.color = ft.colors.ERROR
            else:
                register_user(username, password)
                message.value = "Регистрация успешна. Войдите."
                message.color = ft.colors.GREEN
                set_register_mode(False)
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

    form_card = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=56, color=ft.colors.PRIMARY)],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                title,
                username_field,
                password_field,
                password_repeat_field,
                message,
                action_button,
                switch_button,
                ft.Text(
                    "Нажимая «Зарегистрироваться», вы соглашаетесь с "
                    "условиями использования и политикой конфиденциальности.",
                    size=11,
                    color="rgba(128,128,128,0.8)",  # <-- исправлено!
                    text_align=ft.TextAlign.CENTER,
                    visible=mode["register"],
                ),
            ],
            spacing=18,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=40,
        border_radius=18,
        bgcolor="rgba(255,255,255,0.97)",
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=18,
            color="rgba(25, 118, 210, 0.1)",
            offset=ft.Offset(0, 6),
        ),
        width=400,
        margin=ft.margin.only(top=60, bottom=60),
    )

    return ft.Stack(
        [
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[ft.colors.BLUE_100, ft.colors.INDIGO_100, ft.colors.WHITE],
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