import flet as ft
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import sqlite3

# Массив групп мышц — важно! Используй такие же значения, как в базе!
MUSCLE_GROUPS = [
    "Грудь", "Бицепс", "Трицепс", "Спина", "Трапеция", "Дельты", "Пресс", "Ноги"
]

def radar_chart_image(data, labels):
    num_vars = len(data)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
    ax.plot(angles, data, color="#2196f3", linewidth=2)
    ax.fill(angles, data, color="#2196f3", alpha=0.25)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=11, color="#fff")
    ax.spines["polar"].set_color("#666")
    ax.set_facecolor("#222")
    fig.patch.set_facecolor("#222")
    plt.tight_layout(pad=2)

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", transparent=True)
    plt.close(fig)
    buf.seek(0)
    img_bytes = buf.read()
    img_b64 = base64.b64encode(img_bytes).decode("utf-8")
    return img_b64

def get_muscle_group_counts(username):
    # Возвращает массив: сколько упражнений для каждой группы мышц
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    counts = []
    for group in MUSCLE_GROUPS:
        cursor.execute(
            "SELECT COUNT(*) FROM workouts WHERE username = ? AND muscle_group = ?",
            (username, group)
        )
        val = cursor.fetchone()[0]
        counts.append(val)
    conn.close()
    return counts

def progress_page(page):
    username = page.session.get("username")  # Получение текущего пользователя из сессии

    # Получаем данные из базы
    if username:
        values = get_muscle_group_counts(username)
    else:
        values = [0] * len(MUSCLE_GROUPS)

    radar_img_b64 = radar_chart_image(values.copy(), MUSCLE_GROUPS)

    # Имитация вкладок через кнопки (оставим, но график реагирует только на пользователя)
    def switch_tab(e):
        selected_tab = e.control.text
        for btn in tab_buttons.controls:
            btn.style = ft.ButtonStyle(
                bgcolor=ft.colors.DEEP_ORANGE_300 if btn.text == selected_tab else ft.colors.GREY_700,
                color=ft.colors.WHITE
            )
        page.update()

    tab_buttons = ft.Row(
        [
            ft.ElevatedButton(
                text="Обзор",
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.DEEP_ORANGE_300,
                    color=ft.colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=8)
                ),
                on_click=switch_tab
            ),
            ft.ElevatedButton(
                text="Упражнения",
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.GREY_700,
                    color=ft.colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=8)
                ),
                on_click=switch_tab
            ),
            ft.ElevatedButton(
                text="Меры",
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.GREY_700,
                    color=ft.colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=8)
                ),
                on_click=switch_tab
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    return ft.Column(
        [
            tab_buttons,
            ft.Container(height=8),
            ft.Text("Этот месяц", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text(
                "Определите области, которым требуется больше внимания",
                size=14,
                color=ft.colors.GREY_400,
            ),
            ft.Container(height=16),

            # Радарный график
            ft.Container(
                ft.Image(src_base64=radar_img_b64, width=300, height=300, fit=ft.ImageFit.CONTAIN),
                alignment=ft.alignment.center,
                bgcolor="#000000",
                border_radius=12,
                padding=10,
            ),

            ft.Container(height=24),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )