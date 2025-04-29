import flet as ft
import sqlite3
from datetime import date

# Инициализация таблицы замеров
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS measurements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        body_part TEXT NOT NULL,
        value REAL NOT NULL,
        measurement_date DATE NOT NULL
    )
''')
conn.commit()
conn.close()

# Функция для добавления замера в базу данных
def insert_measurement(username, body_part, value):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO measurements (username, body_part, value, measurement_date)
        VALUES (?, ?, ?, ?)
    """, (username, body_part, value, str(date.today())))
    conn.commit()
    conn.close()

# Функция для получения замеров по части тела
def get_measurements_by_part(username, body_part):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT measurement_date, value FROM measurements
        WHERE username = ? AND body_part = ?
        ORDER BY measurement_date
    """, (username, body_part))
    rows = cursor.fetchall()
    conn.close()
    return rows

# Страница замеров
def measurements_page(page, username):
    selected_part = ft.Dropdown(
        options=[
            ft.DropdownOption("Вес"),
            ft.DropdownOption("Грудь"),
            ft.DropdownOption("Талия"),
            ft.DropdownOption("Бедро"),
            ft.DropdownOption("Рука"),
            ft.DropdownOption("Процент жира")
        ],
        width=200,
        value="Вес"
    )

    chart = ft.LineChart(
        width=350,
        height=200,
        tooltip_bgcolor=ft.colors.DEEP_ORANGE,
        left_axis=ft.ChartAxis(title=ft.Text("см/кг/проценты"))
    )

    def update_chart(e=None):
        chart.data_series.clear()
        data = get_measurements_by_part(username, selected_part.value)
        chart.data_series.append(
            ft.LineChartData(
                data_points=[ft.LineChartDataPoint(x=i, y=row[1]) for i, row in enumerate(data)],
                stroke_width=3,
                color=ft.colors.BLUE
            )
        )
        page.update()

    def open_add_dialog(e):
        dialog = ft.AlertDialog(modal=True)
        input_value = ft.TextField(label="Значение", keyboard_type=ft.KeyboardType.NUMBER)

        def save_measurement(e):
            try:
                val = float(input_value.value)
                insert_measurement(username, selected_part.value, val)
                dialog.open = False
                update_chart()
                page.update()
            except ValueError:
                input_value.error_text = "Введите число"
                page.update()

        dialog.title = ft.Text("Добавить замер")
        dialog.content = input_value
        dialog.actions = [
            ft.TextButton("Отмена", on_click=lambda e: setattr(dialog, "open", False)),
            ft.TextButton("Сохранить", on_click=save_measurement)
        ]
        page.dialog = dialog
        dialog.open = True
        page.update()

    add_button = ft.ElevatedButton("Добавить замер", icon=ft.icons.ADD, on_click=open_add_dialog)

    content = ft.Column([
        ft.Text("Замеры тела", size=22, weight=ft.FontWeight.BOLD),
        selected_part,
        add_button,
        chart
    ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    selected_part.on_change = update_chart
    update_chart()

    return ft.Container(content=content, padding=10, alignment=ft.alignment.top_center)
