import flet as ft

def plan_gym(page: ft.Page, content_area: ft.Column, go_back):
    content_area.controls.clear()

    # Статический заголовок
    title_text = ft.Text(
        "План: Домашний спортзал",
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
            description="Этот 8-недельный план для домашних тренировок поможет развить силу и выносливость.\n"
                        "Что нужно:\n"
                        "• 3 тренировки в неделю (понедельник, среда, пятница) по 45–60 минут.\n"
                        "• Оборудование: гантели (или бутылки с водой), стул, эспандер (или полотенце).\n"
                        "• Питание: профицит для набора, дефицит для сушки.\n"
                        "• Сон 7–8 часов, 1.5–2 л воды в день.",
            icon=ft.icons.INFO_OUTLINE,
            width=320,
            height=260,
        ),
        # Расписание
        create_card(
            title="Расписание",
            description="Тренировки 3 раза в неделю:\n"
                        "• Понедельник: Грудь + Трицепс.\n"
                        "• Среда: Спина + Бицепс.\n"
                        "• Пятница: Ноги + Плечи.\n"
                        "Каждая тренировка включает:\n"
                        "• Разминка: 5–7 мин.\n"
                        "• Основная часть: 30–40 мин (6 упражнений).\n"
                        "• Заминка: 5 мин.",
            icon=ft.icons.CALENDAR_TODAY,
            width=320,
            height=240,
        ),
        # Разминка
        create_card(
            title="Разминка (5–7 минут)",
            description="Подготовьте тело:\n"
                        "1. Прыжки на месте: 1 мин.\n"
                        "2. Вращения плечами: 30 сек в каждую сторону.\n"
                        "3. Приседания без веса: 15 повторений.\n"
                        "4. Наклоны в стороны: 10 раз на сторону.\n"
                        "5. Поза кошки-коровы: 1 мин.",
            icon=ft.icons.DIRECTIONS_RUN,
            width=320,
            height=240,
        ),
        # День 1: Грудь + Трицепс
        create_card(
            title="День 1: Отжимания",
            description="Подходы: 3 по 10–15 повторений. Отдых: 45–60 сек.\n"
                        "• Упор лёжа, руки на ширине плеч.\n"
                        "• Опускайтесь, пока грудь почти не коснётся пола.\n"
                        "• Совет: держите тело прямым, напрягайте пресс.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F06621101-Push-up-m_Chest-FIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Отжимания с узкой постановкой",
            description="Подходы: 3 по 8–12 повторений. Отдых: 45 сек.\n"
                        "• Руки близко друг к другу, локти вдоль тела.\n"
                        "• Опускайтесь, напрягая трицепсы.\n"
                        "• Совет: не разводите локти, держите тело прямым.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02831101-Diamond-Push-up_Upper-Arms-FIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Разводка с бутылками",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Лягте на пол, бутылки с водой в руках.\n"
                        "• Разводите руки в стороны, слегка сгибая локти.\n"
                        "• Совет: двигайтесь медленно, чувствуйте грудь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03081101-Dumbbell-Fly_Chest-FIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Обратные отжимания от стула",
            description="Подходы: 3 по 10–12 повторений. Отдых: 45 сек.\n"
                        "• Сядьте на пол, руки на стуле позади, ноги вытянуты.\n"
                        "• Поднимайте тело, сгибая локти.\n"
                        "• Совет: держите локти направленными назад.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F34431101-Dip-on-Floor-with-Chair_Chest_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Разгибания рук с бутылкой",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Встаньте, бутылка над головой, руки выпрямлены.\n"
                        "• Сгибайте локти, опуская бутылку за голову.\n"
                        "• Совет: держите локти неподвижно, работайте трицепсом.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04301101-Dumbbell-Standing-Triceps-Extension_Upper-Arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Отжимания с упором сзади",
            description="Подходы: 3 по 10–12 повторений. Отдых: 45 сек.\n"
                        "• Упор лёжа, руки на стуле позади.\n"
                        "• Опускайтесь, сгибая локти, напрягая трицепс.\n"
                        "• Совет: держите тело прямым, не прогибайтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F01361101-Push-Up_Chest_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        # День 2: Спина + Бицепс
        create_card(
            title="День 2: Тяга бутылок в наклоне",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45–60 сек.\n"
                        "• Наклонитесь, спина прямая, бутылки в руках.\n"
                        "• Тяните бутылки к поясу, сводя лопатки.\n"
                        "• Совет: не округляйте спину, работайте спиной.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02921101-Dumbbell-Bent-over-Row_back_Back-AFIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Супермен",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Лягте лицом вниз, руки вытянуты вперёд.\n"
                        "• Поднимайте руки, грудь и ноги одновременно.\n"
                        "• Совет: задержитесь на 1–2 сек вверху.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F49391101-Superman-Row-(female)_Back_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Тяга эспандера (или полотенца)",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Встаньте, эспандер или полотенце под ногами.\n"
                        "• Тяните концы к груди, сводя лопатки.\n"
                        "• Совет: держите спину прямой, не наклоняйтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00271101-Barbell-Bent-Over-Row_Back-FIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Сгибания с бутылками",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Встаньте, бутылки в руках, локти прижаты.\n"
                        "• Сгибайте руки, поднимая бутылки к плечам.\n"
                        "• Совет: не раскачивайтесь, работайте бицепсом.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02851101-Dumbbell-Alternate-Biceps-Curl_Upper-Arms-AFIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Сгибания молот с бутылками",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Бутылки в руках, хват нейтральный.\n"
                        "• Сгибайте руки, поднимая бутылки к плечам.\n"
                        "• Совет: держите локти неподвижно.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02941101-Dumbbell-Biceps-Curl_Upper-Arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Изометрические сгибания",
            description="Подходы: 3 по 20–30 сек. Отдых: 45 сек.\n"
                        "• Держите бутылки, согнув руки под углом 90°.\n"
                        "• Напрягайте бицепсы, не двигая руками.\n"
                        "• Совет: дышите ровно, фокусируйтесь на напряжении.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03121101-Dumbbell-Hammer-Curl-II_Upper-Arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        # День 3: Ноги + Плечи
        create_card(
            title="День 3: Приседания с весом тела",
            description="Подходы: 3 по 15–20 повторений. Отдых: 45–60 сек.\n"
                        "• Встаньте, ноги на ширине плеч.\n"
                        "• Приседайте до параллели бёдер с полом.\n"
                        "• Совет: держите спину прямой, колени в линии с носками.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F63361101-Bodyweight-Slow-To-Explosive-Squats-(male)_Hips_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Выпады",
            description="Подходы: 3 по 12 повторений на ногу. Отдых: 45 сек.\n"
                        "• Шаг вперёд, заднее колено почти касается пола.\n"
                        "• Возвращайтесь в исходное положение.\n"
                        "• Совет: держите корпус прямым, не наклоняйтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F09091101-Band-Lunges_Thighs_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Подъёмы на носки",
            description="Подходы: 3 по 15–20 повторений. Отдых: 45 сек.\n"
                        "• Встаньте, поднимайтесь на носки.\n"
                        "• Медленно опускайтесь, растягивая икры.\n"
                        "• Совет: для сложности держите бутылки в руках.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F13731101-Bodyweight-Standing-Calf-Raise_Calves_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Жим бутылок над головой",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Встаньте, бутылки на уровне плеч.\n"
                        "• Выжимайте бутылки вверх, выпрямляя руки.\n"
                        "• Совет: напрягайте пресс, не прогибайтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04051101-Dumbbell-Seated-Shoulder-Press_Shoulders_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Подъёмы бутылок через стороны",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Бутылки в руках, поднимайте до уровня плеч.\n"
                        "• Слегка сгибайте локти, медленно опускайте.\n"
                        "• Совет: не используйте инерцию, работайте плечами.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03341101-Dumbbell-Lateral-Raise_shoulder-AFIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Планка с подъёмом рук",
            description="Подходы: 3 по 10–12 повторений на сторону. Отдых: 45 сек.\n"
                        "• Упор лёжа на предплечьях, тело прямое.\n"
                        "• Поочерёдно поднимайте одну руку вперёд.\n"
                        "• Совет: держите баланс, не раскачивайтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04651101-Front-Plank_Waist_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        # Заминка
        create_card(
            title="Заминка (5 минут)",
            description="Расслабьтесь и восстановитесь:\n"
                        "1. Растяжка груди (руки за спиной): 1 мин.\n"
                        "2. Растяжка спины (поза ребёнка): 1 мин.\n"
                        "3. Растяжка ног (выпады): 30 сек на ногу.\n"
                        "4. Растяжка плеч (рука через грудь): 30 сек на сторону.\n"
                        "5. Глубокое дыхание: 1 мин.",
            icon=ft.icons.SELF_IMPROVEMENT,
            width=320,
            height=260,
        ),
        # Питание
        create_card(
            title="Питание",
            description="Для прогресса:\n"
                        "• Набор: профицит калорий (+300–500 ккал, вес × 35–40 ккал).\n"
                        "• Сушка: дефицит калорий (–300–500 ккал, вес × 25–30 ккал).\n"
                        "• Белок: 1.6–2.2 г/кг (курица, рыба, яйца, творог).\n"
                        "• Углеводы: овсянка, рис, гречка (3–5 г/кг).\n"
                        "• Жиры: орехи, авокадо, масло (0.8–1 г/кг).\n"
                        "• Пример дня: овсянка с ягодами, курица с гречкой, рыба с овощами.",
            icon=ft.icons.RESTAURANT,
            width=320,
            height=280,
        ),
        # Восстановление
        create_card(
            title="Восстановление",
            description="Для прогресса:\n"
                        "• Сон: 7–8 часов в сутки.\n"
                        "• Вода: 1.5–2 л/день, пейте до и после тренировок.\n"
                        "• Отдых: 1–2 дня между тренировками одной группы мышц.\n"
                        "• Растяжка: 5–10 мин после каждой тренировки.\n"
                        "• Стресс: практикуйте дыхательные упражнения (5 мин/день).",
            icon=ft.icons.HEALTH_AND_SAFETY,
            width=320,
            height=240,
        ),
        # Советы для дома
        create_card(
            title="Советы для дома",
            description="Организуйте тренировки:\n"
                        "• Место: выделите 2–3 м², уберите лишние предметы.\n"
                        "• Оборудование: используйте бутылки (1–2 л), полотенце, стул.\n"
                        "• Тайминг: тренируйтесь в одно время для привычки.\n"
                        "• Музыка: включите энергичный плейлист для мотивации.\n"
                        "• Прогресс: увеличивайте повторения или время каждые 2 недели.",
            icon=ft.icons.HOME,
            width=320,
            height=240,
        ),
        # Мотивация
        create_card(
            title="Мотивация и прогресс",
            description="Двигайтесь к цели:\n"
                        "• Фото: делайте каждые 2 недели для сравнения.\n"
                        "• Журнал: записывайте повторения и самочувствие.\n"
                        "• Прогрессия: добавляйте 2–3 повторения каждые 2 недели.\n"
                        "• Цели: ставьте задачи (например, 20 отжиманий без остановки).\n"
                        "• Награда: радуйте себя (новая бутылка, отдых).",
            icon=ft.icons.STAR,
            width=320,
            height=260,
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
        page.title = "План: Домашний спортзал"
        page.bgcolor = ft.colors.BLACK
        content_area = ft.Column()
        plan_gym(page, content_area, lambda e: None)  # Заглушка для go_back
        page.add(content_area)
    ft.app(target=main)