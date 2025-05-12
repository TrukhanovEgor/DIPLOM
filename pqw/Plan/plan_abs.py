import flet as ft

def plan_abs(page: ft.Page, content_area: ft.Column, go_back):
    content_area.controls.clear()

    # Статический заголовок
    title_text = ft.Text(
        "План: Убрать живот",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER,
        font_family="Arial",
    )

    # Кнопка "Назад"
    back_button = ft.ElevatedButton(
        text="Назад",
        on_click=go_back,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.DEEP_ORANGE_300,
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=ft.padding.symmetric(horizontal=20, vertical=10),
        ),
    )

    # Функция для создания карточки
    def create_card(title, description, img_url=None, icon=None, width=320, height=180):
        screen_width = page.window.width if page.window.width > 0 else 350
        scale = min(1.0, screen_width / 400)  # Масштабируем для узких экранов
        card_width = width * scale
        card_height = height * scale

        content = []
        if icon:
            content.append(ft.Icon(icon, color=ft.colors.DEEP_ORANGE_300, size=24 * scale))
        content.extend([
            ft.Text(
                title,
                size=16 * scale,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.WHITE,
                text_align=ft.TextAlign.CENTER,
                font_family="Arial",
                max_lines=2,
                overflow=ft.TextOverflow.ELLIPSIS,
            ),
            ft.Text(
                description,
                size=12 * scale,
                color=ft.colors.WHITE70,
                text_align=ft.TextAlign.LEFT,
                font_family="Arial",
            ),
        ])

        if img_url:
            content.insert(0, ft.Image(
                src=img_url,
                width=card_width,
                height=card_height * 0.5,
                fit=ft.ImageFit.COVER,
                border_radius=12,
                opacity=0.6,
                error_content=ft.Text("Ошибка изображения", color=ft.colors.RED_400, size=12),
            ))

        return ft.Container(
            content=ft.Column(
                content,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8 * scale,
            ),
            padding=10 * scale,
            width=card_width,
            height=card_height,
            margin=ft.margin.all(8 * scale),
            border_radius=12,
            bgcolor=ft.colors.GREY_900,
            gradient=ft.LinearGradient(
                colors=["#B3000000", ft.colors.TRANSPARENT],
                begin=ft.alignment.bottom_center,
                end=ft.alignment.top_center,
            ),
            shadow=[
                ft.BoxShadow(
                    color="#66000000",
                    blur_radius=8 * scale,
                    offset=ft.Offset(0, 4 * scale),
                    spread_radius=1 * scale,
                )
            ],
        )

    # Контент плана тренировок
    cards = [
        # Введение
        create_card(
            title="Введение",
            description="Этот 8-недельный план поможет убрать жир в области живота и укрепить мышцы кора.\n"
                        "Что нужно:\n"
                        "• Тренировки 3–4 раза в неделю по 30–40 минут.\n"
                        "• Дефицит калорий (ешьте меньше, чем тратите).\n"
                        "• Сон 7–8 часов и 1.5–2 л воды в день.\n"
                        "Начните с малого, будьте регулярны!",
            icon=ft.icons.INFO_OUTLINE,
            width=320,
            height=240,
        ),
        # Расписание
        create_card(
            title="Расписание",
            description="• Недели 1–4: тренировки в понедельник, среду, пятницу.\n"
                        "• Недели 5–8: тренировки в понедельник, вторник, четверг, пятницу.\n"
                        "Каждая тренировка включает:\n"
                        "• Разминка: 5–7 мин.\n"
                        "• Основная часть: 20–25 мин.\n"
                        "• Заминка: 5 мин.",
            icon=ft.icons.CALENDAR_TODAY,
            width=320,
            height=220,
        ),
        # Разминка
        create_card(
            title="Разминка (5–7 минут)",
            description="Подготовьте тело к тренировке:\n"
                        "1. Ходьба на месте с высоким подниманием колен: 1 мин.\n"
                        "2. Вращения плечами вперёд и назад: 30 сек в каждую сторону.\n"
                        "3. Наклоны корпуса в стороны: 10 раз на сторону.\n"
                        "4. Прыжки на месте (лёгкие): 1 мин.\n"
                        "5. Поза кошки-коровы (растяжка): 1 мин.",
            icon=ft.icons.DIRECTIONS_RUN,
            width=320,
            height=260,
        ),
        # Недели 1–4: Упражнения
        create_card(
            title="Недели 1–4: Кардио",
            description="Задание: 15 мин кардио (средний темп, пульс 120–140 уд/мин).\n"
                        "• Варианты: бег, велотренажёр, прыжки со скакалкой.\n"
                        "• Совет: дышите ровно, не перенапрягайтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F21971101-Run-on-Treadmill-(female)_Cardio_small.png&w=640&q=100",
            width=320,
            height=220,
        ),
        create_card(
            title="Недели 1–4: Скручивания",
            description="Подходы: 3 по 15–20 повторений. Отдых: 30–45 сек.\n"
                        "• Лягте на спину, согните колени, руки за головой.\n"
                        "• Поднимайте плечи к коленям, напрягая пресс.\n"
                        "• Совет: не тяните шею, работайте мышцами живота.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02741101-Crunch-Floor-m_waist_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="Недели 1–4: Планка",
            description="Подходы: 3 по 30–45 сек. Отдых: 30–45 сек.\n"
                        "• Опора на предплечья и носки, тело прямое.\n"
                        "• Напрягите пресс, не прогибайтесь в пояснице.\n"
                        "• Совет: дышите ровно, смотрите вниз.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04631101-Front-Plank_waist-FIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="Недели 1–4: Велосипед",
            description="Подходы: 3 по 12–15 повторений на сторону. Отдых: 30–45 сек.\n"
                        "• Лягте, поднимите ноги, имитируйте педалирование.\n"
                        "• Касайтесь локтем противоположного колена.\n"
                        "• Совет: держите движения плавными.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F22641101-Stationary-Bike-Run-(version-3)-(female)_Cardio_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        # Недели 5–8: Упражнения
        create_card(
            title="Недели 5–8: Интервальное кардио",
            description="Задание: 15 мин (30 сек спринт, 1 мин ходьба, пульс 140–160 уд/мин).\n"
                        "• Варианты: бег, скакалка, прыжки.\n"
                        "• Совет: увеличивайте интенсивность постепенно.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F05111101-Jump-Rope-(female)_Cardio-FIX_small.png&w=640&q=100",
            width=320,
            height=220,
        ),
        create_card(
            title="Недели 5–8: Подъёмы ног",
            description="Подходы: 3 по 12–15 повторений. Отдых: 20–30 сек.\n"
                        "• Лягте, поднимайте прямые ноги до угла 90°.\n"
                        "• Медленно опускайте, не касаясь пола.\n"
                        "• Совет: держите поясницу прижатой.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02741101-Crunch-Floor-m_waist_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="Недели 5–8: Боковая планка",
            description="Подходы: 3 по 20–30 сек на сторону. Отдых: 20–30 сек.\n"
                        "• Опора на одно предплечье, тело прямое.\n"
                        "• Напрягите боковые мышцы живота.\n"
                        "• Совет: не давайте бёдрам провисать.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F01331101-Bent-Knee-Side-Plank_Waist_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="Недели 5–8: Русский твист",
            description="Подходы: 3 по 15 повторений на сторону. Отдых: 20–30 сек.\n"
                        "• Сядьте, слегка откиньтесь, ноги приподняты.\n"
                        "• Поворачивайте корпус, касаясь пола по сторонам.\n"
                        "• Совет: держите спину прямой.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F06891101-Seated-Leg-Raise_waist_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="Недели 5–8: Скручивания с поворотом",
            description="Подходы: 3 по 12–15 повторений. Отдых: 20–30 сек.\n"
                        "• Лягте, поднимайте плечи, направляя локоть к противоположному колену.\n"
                        "• Чередуйте стороны плавно.\n"
                        "• Совет: не торопитесь, фокусируйтесь на прессе.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04431101-Elbow-to-Knee_waist_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        # Заминка
        create_card(
            title="Заминка (5 минут)",
            description="Расслабьтесь и восстановитесь:\n"
                        "1. Поза ребёнка (растяжка): 1 мин.\n"
                        "2. Наклоны в стороны: 30 сек на сторону.\n"
                        "3. Поза кобры (растяжка спины): 1 мин.\n"
                        "4. Глубокое дыхание (вдох носом, выдох ртом): 1 мин.",
            icon=ft.icons.SELF_IMPROVEMENT,
            width=320,
            height=220,
        ),
        # Питание
        create_card(
            title="Питание",
            description="Для сжигания жира:\n"
                        "• Дефицит калорий: ешьте на 300–500 ккал меньше нормы (вес × 30 ± 500 ккал).\n"
                        "• Белок: 1.6–2 г/кг веса (курица, рыба, яйца, творог).\n"
                        "• Овощи: 400–500 г/день (брокколи, шпинат, кабачки).\n"
                        "• Углеводы: овсянка, гречка, избегайте сахара.\n"
                        "• Жиры: 0.8–1 г/кг (авокадо, орехи).\n"
                        "• Пример дня: овсянка с ягодами, курица с гречкой, рыба с овощами.",
            icon=ft.icons.RESTAURANT,
            width=320,
            height=280,
        ),
        # Образ жизни
        create_card(
            title="Образ жизни",
            description="Поддерживайте результат:\n"
                        "• Сон: 7–8 часов в сутки.\n"
                        "• Вода: 1.5–2 л/день, пейте каждые 2 часа.\n"
                        "• Стресс: 5 мин медитации или дыхания в день.\n"
                        "• Активность: 10–15 мин прогулок ежедневно.\n"
                        "• Регулярность: тренируйтесь даже в лёгком темпе.",
            icon=ft.icons.HEALTH_AND_SAFETY,
            width=320,
            height=240,
        ),
        # Прогресс
        create_card(
            title="Прогресс",
            description="Отслеживайте изменения:\n"
                        "• Фото: каждые 2 недели (спереди и сбоку).\n"
                        "• Объёмы: измеряйте талию раз в неделю.\n"
                        "• Сила: увеличивайте время планки на 5–10 сек каждые 2 недели.\n"
                        "• Дневник: записывайте тренировки и питание.\n"
                        "• Самочувствие: отмечайте энергию и настроение.",
            icon=ft.icons.BAR_CHART,
            width=320,
            height=240,
        ),
    ]

    # Создаем контейнер с вертикальной прокруткой
    content_area.controls.append(
        ft.Column(
            [
                ft.Container(
                    content=ft.Row(
                        [back_button, title_text],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=ft.padding.symmetric(horizontal=10, vertical=10),
                    bgcolor=ft.colors.GREY_800,
                    border_radius=8,
                ),
                ft.ListView(
                    controls=[ft.Row([card], alignment=ft.MainAxisAlignment.CENTER) for card in cards],
                    spacing=10,
                    padding=ft.padding.symmetric(vertical=10, horizontal=10),
                    expand=True,
                    auto_scroll=True,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

    content_area.scroll = ft.ScrollMode.AUTO
    page.update()

if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "План: Убрать живот"
        page.bgcolor = ft.colors.BLACK
        content_area = ft.Column()
        plan_abs(page, content_area, lambda e: None)  # Заглушка для go_back
        page.add(content_area)
    ft.app(target=main)