import flet as ft
from database import register_user, login_user, user_exists

def auth_page(page, on_login_success):
    username_field = ft.TextField(label="Имя пользователя", width=300)
    password_field = ft.TextField(label="Пароль", password=True, can_reveal_password=True, width=300)

    message = ft.Text("", size=14, color=ft.colors.RED)
    mode = {"register": False}

    def switch_mode(e):
        mode["register"] = not mode["register"]
        username_field.value = ""
        password_field.value = ""
        message.value = ""
        update_labels()
        page.update()

    def update_labels():
        if mode["register"]:
            title.value = "Регистрация"
            action_button.text = "Зарегистрироваться"
            switch_button.text = "Уже есть аккаунт? Войти"
        else:
            title.value = "Вход"
            action_button.text = "Войти"
            switch_button.text = "Нет аккаунта? Зарегистрироваться"

    def handle_action(e):
        username = username_field.value.strip()
        password = password_field.value.strip()

        if not username or not password:
            message.value = "Поля не могут быть пустыми."
            message.color = ft.colors.RED
        elif mode["register"]:
            if user_exists(username):
                message.value = "Пользователь с таким именем уже существует."
                message.color = ft.colors.RED
            else:
                register_user(username, password)
                message.value = "Регистрация успешна. Войдите."
                message.color = ft.colors.GREEN
                switch_mode(None)
        else:
            if not user_exists(username):
                message.value = "Такой пользователь не зарегистрирован."
                message.color = ft.colors.RED
            elif login_user(username, password):
                message.value = "Успешный вход!"
                message.color = ft.colors.GREEN
                page.update()
                on_login_success(username)
                return
            else:
                message.value = "Неверный пароль."
                message.color = ft.colors.RED

        page.update()

    title = ft.Text("Вход", size=28, weight=ft.FontWeight.BOLD)
    action_button = ft.ElevatedButton("Войти", on_click=handle_action)
    switch_button = ft.TextButton("Нет аккаунта? Зарегистрироваться", on_click=switch_mode)

    form = ft.Column(
        [
            title,
            username_field,
            password_field,
            message,
            ft.Row([action_button], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([switch_button], alignment=ft.MainAxisAlignment.CENTER)
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    return ft.Container(
        content=form,
        alignment=ft.alignment.center,
        expand=True
    )
