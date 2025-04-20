import flet as ft
from database import register_user, login_user, user_exists

def auth_page(page, on_login_success):
    username_field = ft.TextField(label="Имя пользователя", width=300)
    password_field = ft.TextField(label="Пароль", password=True, can_reveal_password=True, width=300)

    message = ft.Text("", size=14, color=ft.colors.RED)

    def try_register(e):
        username = username_field.value.strip()
        password = password_field.value.strip()

        if not username or not password:
            message.value = "Поля не могут быть пустыми."
            message.color = ft.colors.RED
        elif user_exists(username):
            message.value = "Пользователь с таким именем уже существует."
            message.color = ft.colors.RED
        else:
            register_user(username, password)
            message.value = "Регистрация успешна. Войдите."
            message.color = ft.colors.GREEN
        page.update()

    def try_login(e):
        username = username_field.value.strip()
        password = password_field.value.strip()

        if not username or not password:
            message.value = "Поля не могут быть пустыми."
            message.color = ft.colors.RED
        elif not user_exists(username):
            message.value = "Такой пользователь не зарегистрирован."
            message.color = ft.colors.RED
        elif login_user(username, password):
            message.value = "Успешный вход!"
            message.color = ft.colors.GREEN
            page.update()
            on_login_success()
        else:
            message.value = "Неверный пароль."
            message.color = ft.colors.RED
        page.update()

    return ft.Column(
        [
            ft.Text("Вход / Регистрация", size=24, weight=ft.FontWeight.BOLD),
            username_field,
            password_field,
            ft.Row([
                ft.ElevatedButton("Войти", on_click=try_login),
                ft.TextButton("Регистрация", on_click=try_register)
            ]),
            message
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
