import flet as ft

def plan_fitness_club(page: ft.Page, content_area: ft.Column, go_back):
    content_area.controls.clear()

    # Статический заголовок
    title_text = ft.Text(
        "План: Фитнес-клуб",
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
            description="Этот 8-недельный план для фитнес-клуба поможет набрать мышечную массу и силу.\n"
                        "Что нужно:\n"
                        "• 3 тренировки в неделю (понедельник, среда, пятница) по 60–75 минут.\n"
                        "• Постепенное увеличение веса каждые 2 недели.\n"
                        "• Питание с профицитом калорий (для набора массы) или дефицитом (для сушки).\n"
                        "• Сон 7–8 часов и 1.5–2 л воды в день.",
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
                        "• Основная часть: 45–50 мин (6 упражнений).\n"
                        "• Заминка: 5 мин.",
            icon=ft.icons.CALENDAR_TODAY,
            width=320,
            height=240,
        ),
        # Разминка
        create_card(
            title="Разминка (5–7 минут)",
            description="Подготовьте мышцы и суставы:\n"
                        "1. Бег на дорожке (лёгкий темп): 2 мин.\n"
                        "2. Вращения плечами и руками: 30 сек в каждую сторону.\n"
                        "3. Приседания без веса: 15 повторений.\n"
                        "4. Наклоны корпуса в стороны: 10 раз на сторону.\n"
                        "5. Растяжка груди/спины (поза кошки): 1 мин.",
            icon=ft.icons.DIRECTIONS_RUN,
            width=320,
            height=260,
        ),
        # День 1: Грудь + Трицепс
        create_card(
            title="День 1: Жим штанги лёжа",
            description="Подходы: 3 по 8–12 повторений. Отдых: 60–90 сек.\n"
                        "• Лягте на скамью, штанга над грудью.\n"
                        "• Опускайте штангу к середине груди, выжимайте вверх.\n"
                        "• Совет: держите локти под углом 45°, не отрывайте поясницу.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00251101-Barbell-Bench-Press_Chest-FIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Жим гантелей на наклонной скамье",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60 сек.\n"
                        "• Скамья под углом 30–45°, гантели в руках.\n"
                        "• Выжимайте гантели вверх, медленно опускайте.\n"
                        "• Совет: не разводите локти широко, фокусируйтесь на груди.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03141101-Dumbbell-Incline-Bench-Press_Chest_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Разводка гантелей",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Лягте на скамью, гантели над грудью.\n"
                        "• Разводите руки в стороны, слегка сгибая локти.\n"
                        "• Совет: чувствуйте растяжение груди, не опускайте слишком низко.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03081101-Dumbbell-Fly_Chest-FIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Французский жим",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60 сек.\n"
                        "• Лягте на скамью, штанга или EZ-гриф над головой.\n"
                        "• Сгибайте локти, опуская гриф ко лбу.\n"
                        "• Совет: держите локти неподвижно, работайте трицепсом.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00601101-Barbell-Lying-Triceps-Extension-Skull-Crusher_Triceps-SFIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Разгибания на блоке",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Встаньте у блочного тренажёра, рукоять в руках.\n"
                        "• Разгибайте руки вниз, напрягая трицепс.\n"
                        "• Совет: не раскачивайтесь, держите локти прижатыми.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02001101-Cable-Pushdown-(with-rope-attachment)_Upper-Arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Отжимания на брусьях",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60 сек.\n"
                        "• Держитесь за брусья, тело слегка наклонено вперёд.\n"
                        "• Опускайтесь, сгибая локти, затем выжимайте вверх.\n"
                        "• Совет: для трицепса держите тело вертикально.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00191101-Assisted-Triceps-Dip-(kneeling)_Upper-Arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        # День 2: Спина + Бицепс
        create_card(
            title="День 2: Подтягивания",
            description="Подходы: 3 по 6–10 повторений. Отдых: 90 сек.\n"
                        "• Хват шире плеч, подтягивайтесь до подбородка.\n"
                        "• Опускайтесь плавно, полностью выпрямляя руки.\n"
                        "• Совет: используйте ленты, если тяжело.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F06521101-Pull-up_Back_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Тяга штанги в наклоне",
            description="Подходы: 3 по 8–12 повторений. Отдых: 60–90 сек.\n"
                        "• Наклонитесь, спина прямая, штанга в руках.\n"
                        "• Тяните штангу к поясу, сводя лопатки.\n"
                        "• Совет: не округляйте спину, работайте спиной.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00271101-Barbell-Bent-Over-Row_Back-FIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Тяга верхнего блока",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60 сек.\n"
                        "• Сядьте, хват шире плеч, тяните рукоять к груди.\n"
                        "• Сводите лопатки, медленно возвращайтесь.\n"
                        "• Совет: не наклоняйтесь назад, держите корпус прямым.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F01501101-Cable-Bar-Lateral-Pulldown_Back_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Сгибания со штангой",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60 сек.\n"
                        "• Встаньте, штанга в руках, локти прижаты.\n"
                        "• Сгибайте руки, поднимая штангу к плечам.\n"
                        "• Совет: не раскачивайтесь, работайте бицепсом.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00311101-Barbell-Curl_Upper-Arms-FIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Сгибания с гантелями (молот)",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Гантели в руках, хват нейтральный.\n"
                        "• Сгибайте руки, поднимая гантели к плечам.\n"
                        "• Совет: держите локти неподвижно.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03131101-Dumbbell-Hammer-Curl_Forearm_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Концентрированные сгибания",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Сядьте, гантель в одной руке, локоть на бедре.\n"
                        "• Сгибайте руку, напрягая бицепс.\n"
                        "• Совет: выполняйте медленно для максимального эффекта.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02971101-Dumbbell-Concentration-Curl_Upper-Arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        # День 3: Ноги + Плечи
        create_card(
            title="День 3: Приседания со штангой",
            description="Подходы: 3 по 8–12 повторений. Отдых: 90–120 сек.\n"
                        "• Штанга на плечах, спина прямая.\n"
                        "• Приседайте до параллели бёдер с полом.\n"
                        "• Совет: держите колени в линии с носками.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00431101-Barbell-Full-Squat_Thighs_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Жим ногами",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60–90 сек.\n"
                        "• Сядьте в тренажёр, стопы на платформе.\n"
                        "• Выжимайте платформу, не разгибая колени полностью.\n"
                        "• Совет: не отрывайте поясницу от сиденья.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F07401101-Sled-45-Leg-Wide-Press_Thighs_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Выпады с гантелями",
            description="Подходы: 3 по 12 повторений на ногу. Отдых: 60 сек.\n"
                        "• Гантели в руках, шаг вперёд, колено почти касается пола.\n"
                        "• Возвращайтесь в исходное положение.\n"
                        "• Совет: держите корпус прямым, не наклоняйтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02911101-Dumbbell-Bench-Squat_thighs_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Жим штанги стоя",
            description="Подходы: 3 по 8–12 повторений. Отдых: 60–90 сек.\n"
                        "• Штанга на груди, выжимайте вверх.\n"
                        "• Опускайте медленно до уровня плеч.\n"
                        "• Совет: напрягайте пресс, не прогибайтесь в пояснице.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F11651101-Barbell-Standing-Military-Press-(without-rack)_Shoulders-FIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Подъёмы гантелей через стороны",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Гантели в руках, поднимайте до уровня плеч.\n"
                        "• Слегка сгибайте локти, медленно опускайте.\n"
                        "• Совет: не используйте инерцию, работайте плечами.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03341101-Dumbbell-Lateral-Raise_shoulder-AFIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Тяга штанги к подбородку",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60 сек.\n"
                        "• Узкий хват, тяните штангу к подбородку.\n"
                        "• Локти поднимайте выше плеч.\n"
                        "• Совет: не раскачивайтесь, держите движение плавным.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F01201101-Barbell-Upright-Row_shoulder_small.png&w=640&q=100",
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
            description="Для набора массы или сушки:\n"
                        "• Набор: профицит калорий (+300–500 ккал, вес × 35–40 ккал).\n"
                        "• Сушка: дефицит калорий (–300–500 ккал, вес × 25–30 ккал).\n"
                        "• Белок: 1.6–2.2 г/кг (курица, рыба, яйца, протеин).\n"
                        "• Углеводы: овсянка, рис, картофель (3–5 г/кг).\n"
                        "• Жиры: орехи, авокадо, масло (0.8–1 г/кг).\n"
                        "• Пример дня: овсянка с бананом, курица с рисом, рыба с овощами.",
            icon=ft.icons.RESTAURANT,
            width=320,
            height=280,
        ),
        # Восстановление
        create_card(
            title="Восстановление",
            description="Для прогресса:\n"
                        "• Сон: 7–8 часов в сутки.\n"
                        "• Вода: 2–3 л/день, особенно после тренировок.\n"
                        "• Отдых: 1–2 дня между тренировками одной группы мышц.\n"
                        "• Растяжка: 10 мин после каждой тренировки.\n"
                        "• Стресс: избегайте переутомления, делайте дыхательные упражнения.",
            icon=ft.icons.HEALTH_AND_SAFETY,
            width=320,
            height=240,
        ),
        # Мотивация
        create_card(
            title="Мотивация и прогресс",
            description="Двигайтесь к цели:\n"
                        "• Фото: делайте каждые 2 недели для сравнения.\n"
                        "• Журнал: записывайте веса и повторения.\n"
                        "• Прогрессия: увеличивайте вес на 5–10% каждые 2 недели.\n"
                        "• Цели: ставьте маленькие задачи (например, +1 повторение).\n"
                        "• Награда: радуйте себя за достижения (новая экипировка, отдых).",
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
        page.title = "План: Фитнес-клуб"
        page.bgcolor = ft.colors.BLACK
        content_area = ft.Column()
        plan_fitness_club(page, content_area, lambda e: None)  # Заглушка для go_back
        page.add(content_area)
    ft.app(target=main)