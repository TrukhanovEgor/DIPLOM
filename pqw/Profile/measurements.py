import flet as ft
from datetime import datetime
from database import save_measurement, get_user_measurements

def measurements(page, logout_callback, username, return_to_profile):
    selected_index = 0
    selected_param = ["Вес", "Процент жира в организме %", "Грудь"]
    selected_text = ft.Text(selected_param[selected_index], size=18, weight=ft.FontWeight.BOLD)

    # Define units for each parameter
    units = {
        "Вес": "кг",
        "Процент жира в организме %": "%",
        "Грудь": "см"
    }

    def go_back(e):
        page.views.pop()
        page.update()


    def on_param_click(index):
        def handler(e):
            nonlocal selected_index
            selected_index = index
            selected_text.value = selected_param[index]
            value_input.label = f"Введите {selected_param[index].lower()}"
            for i, button in enumerate(param_buttons.controls):
                button.__setattr__("style", ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)))
                if i == index:
                    button.__setattr__("content", ft.Text(selected_param[i], color=ft.colors.WHITE))
                    button.__setattr__("bgcolor", ft.colors.BLUE_700)
                else:
                    button.__setattr__("content", ft.Text(selected_param[i]))
                    button.__setattr__("bgcolor", None)
            refresh_history_and_graph()
            page.update()
        return handler

    def add_measurement(e):
        try:
            value = float(value_input.value)
            if value < 0:
                raise ValueError("Value cannot be negative")
            date = datetime.now().strftime("%Y-%m-%d")
            save_measurement(username, selected_param[selected_index], date, value)
            value_input.value = ""
            refresh_history_and_graph()
        except ValueError:
            page.snack_bar = ft.SnackBar(
                ft.Text("Введите корректное положительное число для замера!")
            )
            page.snack_bar.open = True
            page.update()

    def refresh_history_and_graph():
        history.controls = [
            ft.ListTile(
                leading=ft.Icon(ft.icons.HISTORY),
                title=ft.Text("История замеров"),
                trailing=ft.ElevatedButton(
                    "Добавить",
                    icon=ft.icons.ADD,
                    on_click=add_measurement,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        bgcolor=ft.colors.BLUE_700
                    )
                ),
    ),
        ]

        measurements_data = get_user_measurements(username, selected_param[selected_index])
        if measurements_data:
            for date, value in measurements_data:
                history.controls.append(
                    ft.ListTile(
                        title=ft.Text(date),
                        trailing=ft.Text(f"{value} {units[selected_param[selected_index]]}"),
                    )
                )
        else:
            history.controls.append(
                ft.ListTile(
                    title=ft.Text("Нет записей", color=ft.colors.GREY),
                    subtitle=ft.Text("Добавьте замеры, чтобы увидеть историю", size=12)
                )
            )

        points = measurements_data
        if len(points) >= 1:
            values = [v for _, v in points]
            max_val = max(values) * 1.2 if max(values) > 0 else 1
            bars = []

            for date, value in points:
                height_percent = (value / max_val) if max_val != 0 else 0
                bars.append(
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(f"{value}", size=10, color=ft.colors.WHITE),
                            ft.Container(
                                width=30,
                                height=150 * height_percent,
                                bgcolor=ft.colors.BLUE_700,
                                border_radius=5
                            ),
                            ft.Text(
                                datetime.strptime(date, "%Y-%m-%d").strftime("%d-%m"),
                                size=10,
                                color=ft.colors.WHITE
                            )
                        ],
                        expand=True
                    )
                )

            graph_placeholder.content = ft.Container(
                content=ft.Row(
                    controls=bars,
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    scroll=ft.ScrollMode.ALWAYS
                ),
                height=200,
                expand=True,
                bgcolor=ft.colors.BLACK
            )
        else:
            graph_placeholder.content = ft.Text(
                "Добавьте замеры для отображения графика",
                color=ft.colors.GREY,
                text_align=ft.TextAlign.CENTER
            )

        page.update()

    app_bar = ft.AppBar(
        title=ft.Text("Замеры", size=20, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLACK,
        leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=go_back, icon_color=ft.colors.WHITE),
    )

    param_buttons = ft.Row(
        controls=[
            ft.ElevatedButton(
                content=ft.Text("Вес", color=ft.colors.WHITE),
                on_click=on_param_click(0),
                bgcolor=ft.colors.BLUE_700,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
            ),
            ft.ElevatedButton(
                content=ft.Text("Процент жира в организме %"),
                on_click=on_param_click(1),
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
            ),
            ft.ElevatedButton(
                content=ft.Text("Грудь"),
                on_click=on_param_click(2),
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO
    )

    value_input = ft.TextField(
        label=f"Введите {selected_param[selected_index].lower()}",
        keyboard_type=ft.KeyboardType.NUMBER,
        text_align=ft.TextAlign.CENTER,
        border_color=ft.colors.WHITE,
        text_style=ft.TextStyle(color=ft.colors.WHITE)
    )

    graph_placeholder = ft.Container(
        content=ft.Text("График пока пуст", color=ft.colors.GREY),
        height=200,
        alignment=ft.alignment.bottom_center,
        bgcolor=ft.colors.with_opacity(0.05, ft.colors.WHITE)
    )

    history = ft.Column()

    content = ft.Column(
        controls=[
            selected_text,
            param_buttons,
            value_input,
            graph_placeholder,
            ft.Divider(color=ft.colors.WHITE),
            history
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    page.views.append(
        ft.View(
            "/measurements",
            controls=[app_bar, content],
            bgcolor=ft.colors.BLACK
        )
    )

    refresh_history_and_graph()
    page.update()