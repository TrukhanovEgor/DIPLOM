import flet as ft
import sqlite3

def change_username_in_db(old_username, new_username):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET username = ? WHERE username = ?", (new_username, old_username))
        cursor.execute("UPDATE workouts SET username = ? WHERE username = ?", (new_username, old_username))
        cursor.execute("UPDATE measurements SET username = ? WHERE username = ?", (new_username, old_username))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def settings_page(page, username, return_to_profile=None, on_logout=None):
    # Вынесите создание appbar наружу, не создавайте его здесь!
    # page.appbar = ft.AppBar(...)

    snack_bar = ft.SnackBar(content=ft.Text("", color=ft.colors.WHITE), bgcolor=ft.colors.GREEN_400)
    def show_snack(msg, color=ft.colors.GREEN_400):
        snack_bar.content.value = msg
        snack_bar.bgcolor = color
        page.snack_bar = snack_bar
        snack_bar.open = True
        page.update()

    username_field = ft.TextField(
        label="Новое имя пользователя",
        prefix_icon=ft.icons.PERSON,
        width=320,
        border_radius=8,
        filled=True,
        bgcolor=ft.colors.GREY_100,
        color=ft.colors.BLACK
    )

    def try_change_username():
        new_name = username_field.value.strip()
        if not new_name:
            show_snack("Введите новое имя пользователя", ft.colors.RED_400)
            return
        if new_name == username:
            show_snack("Имя не изменено", ft.colors.RED_400)
            return
        if change_username_in_db(username, new_name):
            show_snack("Имя пользователя изменено!\nВойдите заново.", ft.colors.GREEN_400)
            if on_logout:
                on_logout()
        else:
            show_snack("Имя уже занято!", ft.colors.RED_400)

    username_btn = ft.FilledButton(
        "Сменить имя пользователя",
        icon=ft.icons.SAVE,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.DEEP_ORANGE_400,
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
        on_click=lambda e: try_change_username()
    )

    # Кнопка выхода
    logout_btn = ft.FilledButton(
        "Выйти из аккаунта",
        icon=ft.icons.LOGOUT,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.RED_400,
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
        on_click=lambda e: on_logout() if on_logout else None
    )

    # Оформление и скролл
    scrollable_content = ft.Container(
        bgcolor="rgba(255,255,255,0.96)",
        border_radius=14,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color="rgba(255,140,0,0.15)",
            offset=ft.Offset(0, 8)
        ),
        padding=30,
        margin=30,
        content=ft.Column([
            ft.Text("Аккаунт", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_900),
            ft.Text("Смена имени пользователя:", size=14),
            username_field,
            username_btn,
            ft.Divider(),
            logout_btn,
        ], spacing=18, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

    # Скроллируемый layout
    return ft.ListView(
        controls=[scrollable_content],
        spacing=0,
        padding=0,
        expand=True,
        auto_scroll=False
    )