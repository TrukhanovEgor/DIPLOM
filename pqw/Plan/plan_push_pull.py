import flet as ft

def plan_push_pull(page: ft.Page, content_area: ft.Column, go_back, username=None, go_to_journal=None):
    content_area.controls.clear()

    # Статический заголовок
    title_text = ft.Text(
        "Силовые упражнения для верха тела: Жим и Тяги",
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

        # Контент для текста и иконки
        text_content = []
        if icon:
            text_content.append(ft.Icon(icon, color=ft.colors.DEEP_ORANGE_300, size=24 * scale))
        text_content.extend([
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
                width=card_width - 20 * scale,  # Ограничиваем ширину текста
            ),
        ])

        # Создаём стек для наложения изображения и текста
        stack_content = []
        if img_url:
            stack_content.append(
                ft.Image(
                    src=img_url,
                    width=card_width,
                    height=card_height,
                    fit=ft.ImageFit.COVER,
                    border_radius=12,
                    opacity=0.6,
                    error_content=ft.Text("Ошибка изображения", color=ft.colors.RED_400, size=12),
                )
            )
        stack_content.append(
            ft.Container(
                gradient=ft.LinearGradient(
                    colors=["#B3000000", ft.colors.TRANSPARENT],
                    begin=ft.alignment.bottom_center,
                    end=ft.alignment.top_center,
                ),
                width=card_width,
                height=card_height,
                border_radius=12,
            )
        )
        stack_content.append(
            ft.Column(
                text_content,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8 * scale,
                expand=True,
            )
        )

        return ft.Container(
            content=ft.Stack(stack_content),
            padding=10 * scale,
            width=card_width,
            height=card_height,
            margin=ft.margin.all(8 * scale),
            border_radius=12,
            bgcolor=ft.colors.GREY_900,
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
        create_card(
            title="Введение",
            description="Этот 8-недельный план тренировок разработан для развития силы и мышечной массы верхней части тела в тренажёрном зале. Он включает жимовые (Push) и тяговые (Pull) упражнения, используя штанги, гантели и тренажёры. Тренируйтесь 3 раза в неделю (понедельник, среда, пятница) по 45–60 минут. Соблюдайте технику, питание (профицит для набора, дефицит для сушки) и сон (7–8 часов).",
            icon=ft.icons.INFO_OUTLINE,
            width=320,
            height=260,
        ),
        create_card(
            title="Расписание",
            description="Тренировки 3 раза в неделю:\n"
                        "• Понедельник: Жим (Push) + Ноги\n"
                        "• Среда: Тяги (Pull) + Корпус\n"
                        "• Пятница: Смешанный (Push + Pull)\n"
                        "Каждая тренировка включает:\n"
                        "• Разминка: 5–7 мин\n"
                        "• Основная часть: 30–40 мин (6 упражнений)\n"
                        "• Заминка: 5 мин",
            icon=ft.icons.CALENDAR_TODAY,
            width=320,
            height=240,
        ),
        create_card(
            title="Разминка (5–7 минут)",
            description="Подготовьте мышцы и суставы:\n"
                        "1. Бег на дорожке (лёгкий темп): 2 мин\n"
                        "2. Вращения плечами и локтями: 30 сек в каждую сторону\n"
                        "3. Приседания без веса: 15 повторений\n"
                        "4. Наклоны корпуса в стороны: 10 раз на сторону\n"
                        "5. Растяжка спины (поза кошки): 1 мин",
            icon=ft.icons.DIRECTIONS_RUN,
            width=320,
            height=260,
        ),
        create_card(
            title="День 1: Жим лёжа",
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
            title="День 1: Жим над головой",
            description="Подходы: 3 по 8–12 повторений. Отдых: 60–90 сек.\n"
                        "• Встаньте или сядьте, штанга на уровне плеч.\n"
                        "• Выжимайте штангу вверх, выпрямляя руки.\n"
                        "• Совет: напрягайте пресс, не прогибайтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00911101-Barbell-Seated-Overhead-Press_Shoulders_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Отжимания на брусьях",
            description="Подходы: 3 по 8–12 повторений. Отдых: 60–90 сек.\n"
                        "• Держитесь за брусья, опускайтесь до угла 90° в локтях.\n"
                        "• Выжимайте тело вверх, напрягая трицепсы.\n"
                        "• Совет: для трицепса держите тело вертикально.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F17551101-Weighted-Tricep-Dips_Upper-Arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Разгибания на трицепс",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45–60 сек.\n"
                        "• На блочном тренажёре с канатной рукоятью разгибайте руки вниз.\n"
                        "• Совет: не раскачивайтесь, держите локти неподвижно.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F12271101-Cable-Standing-One-Arm-Tricep-Pushdown-(Overhand-Grip)_Upper-Arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Приседания со штангой",
            description="Подходы: 3 по 8–12 повторений. Отдых: 90–120 сек.\n"
                        "• Штанга на плечах, приседайте до параллели бёдер с полом.\n"
                        "• Совет: держите спину прямой, колени в линии с носками.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00441101-Barbell-Good-Morning_Thighs-AFIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Жим на наклонной скамье",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60–90 сек.\n"
                        "• Скамья под углом 30–45°, выжимайте штангу или гантели вверх.\n"
                        "• Совет: фокусируйтесь на верх груди, не разводите локти широко.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00471101-Barbell-Incline-Bench-Press_Chest-FIX_small.png&w=640&q=100",
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
            title="День 2: Сгибания со штангой",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60 сек.\n"
                        "• Встаньте, штанга в руках, локти прижаты.\n"
                        "• Сгибайте руки, поднимая штангу к плечам.\n"
                        "• Совет: не раскачивайтесь, работайте бицепсом.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F24071101-Barbell-Biceps-Curl-(with-arm-blaster)_Upper-arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Тяга верхнего блока",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60–90 сек.\n"
                        "• Сядьте в тренажёр, тяните рукоять к груди, сводя лопатки.\n"
                        "• Совет: держите корпус прямым, не отклоняйтесь назад.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F22911101-Cable-Wide-Grip-Lat-Pulldown-(female)_Back_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Тяга в тренажёре",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60 сек.\n"
                        "• Сядьте, тяните рукоять к животу, сводя лопатки.\n"
                        "• Совет: не раскачивайтесь, работайте спиной.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02391101-Cable-Straight-Back-Seated-Row_Back_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Скручивания",
            description="Подходы: 3 по 15–20 повторений. Отдых: 30 сек.\n"
                        "• Лягте на коврик, колени согнуты, руки за головой.\n"
                        "• Поднимайте плечи, напрягая пресс.\n"
                        "• Совет: не тяните шею, дышите на подъёме.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02741101-Crunch-Floor-m_waist_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Сгибания молот с гантелями",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Гантели в руках, хват нейтральный.\n"
                        "• Сгибайте руки, поднимая гантели к плечам.\n"
                        "• Совет: держите локти неподвижно.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F03121101-Dumbbell-Hammer-Curl-II_Upper-Arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Жим гантелей лёжа",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60–90 сек.\n"
                        "• Лягте на скамью, гантели в руках над грудью.\n"
                        "• Выжимайте гантели вверх, медленно опускайте.\n"
                        "• Совет: держите локти под углом 45°, фокусируйтесь на груди.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02891101-Dumbbell-Bench-Press_Chest_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Тяга гантели одной рукой",
            description="Подходы: 3 по 12 повторений на руку. Отдых: 45–60 сек.\n"
                        "• Наклонитесь, одна рука опирается, другая с гантелью.\n"
                        "• Тяните гантель к поясу, сводя лопатку.\n"
                        "• Совет: держите спину прямой, не вращайте корпус.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02921101-Dumbbell-Bent-over-Row_back_Back-AFIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Жим Арнольда",
            description="Подходы: 3 по 10–12 повторений. Отдых: 60–90 сек.\n"
                        "• Сядьте, гантели на уровне плеч, ладони к себе.\n"
                        "• Выжимайте гантели вверх, вращая ладони наружу.\n"
                        "• Совет: напрягайте плечи, не прогибайтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04051101-Dumbbell-Seated-Shoulder-Press_Shoulders_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Подтягивания",
            description="Подходы: 3 по 6–10 повторений. Отдых: 90 сек.\n"
                        "• Вис на турнике, подтягивайтесь до подбородка.\n"
                        "• Совет: используйте резиновые ленты, если тяжело.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F06521101-Pull-up_Back_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Отжимания на брусьях (трицепс)",
            description="Подходы: 3 по 8–12 повторений. Отдых: 60–90 сек.\n"
                        "• Держитесь за брусья, опускайтесь, напрягая трицепс.\n"
                        "• Совет: держите тело вертикально, локти вдоль тела.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F00191101-Assisted-Triceps-Dip-(kneeling)_Upper-Arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Сгибания на бицепс в тренажёре",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Сядьте в тренажёр для сгибаний, поднимайте рукоять.\n"
                        "• Совет: не раскачивайтесь, работайте бицепсом.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F05921101-Lever-Preacher-Curl_Upper-Arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="Заминка (5 минут)",
            description="Расслабьтесь и восстановитесь:\n"
                        "1. Растяжка груди (руки за спиной): 1 мин\n"
                        "2. Растяжка спины (поза ребёнка): 1 мин\n"
                        "3. Растяжка ног (выпады): 30 сек на ногу\n"
                        "4. Растяжка плеч (рука через грудь): 30 сек на сторону\n"
                        "5. Глубокое дыхание: 1 мин",
            icon=ft.icons.SELF_IMPROVEMENT,
            width=320,
            height=260,
        ),
        create_card(
            title="Питание",
            description="Для прогресса:\n"
                        "• Набор: профицит калорий (+300–500 ккал, вес × 35–40 ккал)\n"
                        "• Сушка: дефицит калорий (–300–500 ккал, вес × 25–30 ккал)\n"
                        "• Белок: 1.6–2.2 г/кг (курица, рыба, яйца, протеин)\n"
                        "• Углеводы: овсянка, рис, гречка (3–5 г/кг)\n"
                        "• Жиры: орехи, авокадо, масло (0.8–1 г/кг)\n"
                        "• Пример дня: овсянка с бананом, курица с рисом, рыба с овощами",
            icon=ft.icons.RESTAURANT,
            width=320,
            height=280,
        ),
        create_card(
            title="Советы по Push-Pull",
            description="Сбалансируйте тренировки:\n"
                        "• Чередуйте нагрузку: Push и Pull равномерно\n"
                        "• Прогрессия: увеличивайте вес или повторения каждые 2 недели\n"
                        "• Техника: следите за спиной и локтями\n"
                        "• Отдых: 1–2 дня между тренировками одной группы\n"
                        "• Разнообразие: меняйте хват или угол каждые 4 недели",
            icon=ft.icons.FITNESS_CENTER,
            width=320,
            height=240,
        ),
        create_card(
            title="Мотивация и прогресс",
            description="Двигайтесь к цели:\n"
                        "• Журнал: записывайте веса и повторения\n"
                        "• Измерения: объёмы рук, груди каждые 2 недели\n"
                        "• Фото: делайте для сравнения\n"
                        "• Цели: например, жим лёжа с весом 100 кг\n"
                        "• Награда: новая экипировка, отдых",
            icon=ft.icons.STAR,
            width=320,
            height=260,
        ),
    ]

    # Определяем высоту контейнера с защитой от None
    container_height = page.height - 280 if page.height else 850

    # Создаём контейнер с вертикальной прокруткой
    content_area.controls.append(
        ft.Container(
            content=ft.Column(
                controls=[
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
                    ft.Column(
                        controls=[ft.Row([card], alignment=ft.MainAxisAlignment.CENTER) for card in cards],
                        spacing=10,
                        scroll=ft.ScrollMode.AUTO,  # Включаем вертикальный скролл
                        expand=True,
                    ),
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
            height=container_height,
            padding=ft.padding.symmetric(horizontal=10),
            expand=True,
        )
    )

    content_area.expand = True
    page.update()

if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "План: Жим и Тяги"
        page.bgcolor = ft.colors.BLACK
        content_area = ft.Column(expand=True)
        page.add(
            ft.Container(
                content=content_area,
                expand=True,
                padding=ft.padding.all(10),
            )
        )
        plan_push_pull(page, content_area, lambda e: None)  # Заглушка для go_back
    ft.app(target=main)