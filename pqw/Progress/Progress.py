import flet as ft
import sqlite3

MUSCLE_GROUPS = [
    "Грудные мышцы", "Бицепс", "Трицепс", "Широчайшие",
    "Трапеция", "Дельты", "Пресс", "Ноги"
]
SHORT_LABELS = [
    "Грудь", "Бицепс", "Трицепс", "Спина", "Трапеция", "Дельты", "Пресс", "Ноги"
]
BAR_COLORS = [
    ft.colors.BLUE_400, ft.colors.LIGHT_BLUE_400, ft.colors.ORANGE_400,
    ft.colors.DEEP_ORANGE_400, ft.colors.GREEN_400, ft.colors.PURPLE_400,
    ft.colors.PINK_400, ft.colors.LIME_400
]

def get_muscle_group_counts(username):
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
    username = page.session.get("username")
    if username:
        values = get_muscle_group_counts(username)
    else:
        values = [0] * len(MUSCLE_GROUPS)

    groups = [
        ft.BarChartGroup(
            x=i,
            bar_rods=[
                ft.BarChartRod(
                    from_y=0,
                    to_y=count,
                    width=22,
                    color=BAR_COLORS[i % len(BAR_COLORS)],
                    tooltip=f"{label}: {count}",
                )
            ]
        )
        for i, (label, count) in enumerate(zip(SHORT_LABELS, values))
    ]

    max_value = max(values) if values else 1
    min_val = min(values)
    lagging_groups = [label for label, val in zip(SHORT_LABELS, values) if val == min_val and val < max_value]
    lagging_text = ft.Text(
        f"Отстают: {', '.join(lagging_groups) if lagging_groups else 'Нет'}",
        size=16, color=ft.colors.RED_400 if lagging_groups else ft.colors.GREEN_400, weight=ft.FontWeight.BOLD
    )

    def update_chart(_=None):
        new_values = get_muscle_group_counts(username) if username else [0] * len(MUSCLE_GROUPS)
        for i, val in enumerate(new_values):
            groups[i].bar_rods[0].to_y = val
            groups[i].bar_rods[0].tooltip = f"{SHORT_LABELS[i]}: {val}"
        max_value = max(new_values) if new_values else 1
        min_val = min(new_values)
        lagging_groups = [label for label, val in zip(SHORT_LABELS, new_values) if val == min_val and val < max_value]
        lagging_text.value = f"Отстают: {', '.join(lagging_groups) if lagging_groups else 'Нет'}"
        lagging_text.color = ft.colors.RED_400 if lagging_groups else ft.colors.GREEN_400
        page.update()

    refresh_button = ft.IconButton(
        icon=ft.icons.REFRESH,
        icon_color=ft.colors.DEEP_ORANGE_300,
        tooltip="Обновить диаграмму",
        on_click=update_chart,
    )

    # --- ГОРИЗОНТАЛЬНЫЙ СКРОЛЛ ДЛЯ ДИАГРАММЫ ---
    barchart = ft.BarChart(
        bar_groups=groups,
        border=ft.border.all(1, ft.colors.GREY_800),
        left_axis=ft.ChartAxis(
            labels_size=32,
            title=ft.Text("Кол-во тренировок", color=ft.colors.GREY_400),
            title_size=20,
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=i, label=ft.Text(label, color=ft.colors.GREY_300, size=12, weight=ft.FontWeight.BOLD)
                )
                for i, label in enumerate(SHORT_LABELS)
            ],
            labels_size=38,
            title=ft.Text("Группа мышц", color=ft.colors.GREY_400),
            title_size=18,
        ),
        min_y=0,
        max_y=(max_value + 2),
        groups_space=100,
        animate=500,
        tooltip_bgcolor=ft.colors.with_opacity(0.9, ft.colors.BLACK),
        expand=False,
        width=400,  # Делаем шире, чем экран на мобиле
        height=280,
        bgcolor="#181c20"
    )

    barchart_scroll = ft.Row(
        [ft.Container(
            content=barchart,
            padding=10,
            bgcolor="#181c20",
            border_radius=16,
            expand=False,
            width=800  # ширина чуть больше для надписей
        )],
        scroll=ft.ScrollMode.ALWAYS,
        expand=False,
        alignment=ft.MainAxisAlignment.START,
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Row([
                    ft.Text("Прогресс по \n группам мышц", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                    refresh_button
                ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Text(
                    "Сравните, какие группы мышц прорабатываются чаще всего, а какие — реже.",
                    size=16, color=ft.colors.GREY_300
                ),
                barchart_scroll,  # вот тут скроллируется только диаграмма!
                lagging_text,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            scroll=ft.ScrollMode.ALWAYS
        ),
        expand=True,
        bgcolor="#101216"
    )