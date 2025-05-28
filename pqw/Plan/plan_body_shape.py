import flet as ft

def plan_body_shape(page: ft.Page, content_area: ft.Column, go_back, username=None, go_to_journal=None):
    content_area.controls.clear()

    # Статический заголовок
    title_text = ft.Text(
        "План: Стройное тело и гибкость",
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
            description="Этот 8-недельный план поможет сформировать стройное тело и улучшить гибкость.\n"
                        "Что нужно:\n"
                        "• 3 тренировки в неделю (понедельник, среда, пятница) по 45–60 минут.\n"
                        "• Оборудование: коврик, стул, эспандер (или полотенце), бутылки с водой.\n"
                        "• Питание: дефицит калорий для сушки, акцент на белок и овощи.\n"
                        "• Сон 7–8 часов, 1.5–2 л воды в день.",
            icon=ft.icons.INFO_OUTLINE,
            width=320,
            height=260,
        ),
        create_card(
            title="Расписание",
            description="Тренировки 3 раза в неделю:\n"
                        "• Понедельник: Корпус + Ноги.\n"
                        "• Среда: Руки + Спина.\n"
                        "• Пятница: Полное тело + Гибкость.\n"
                        "Каждая тренировка включает:\n"
                        "• Разминка: 5–7 мин (динамическая).\n"
                        "• Основная часть: 30–40 мин (6 упражнений).\n"
                        "• Заминка: 5–10 мин (статическая).",
            icon=ft.icons.CALENDAR_TODAY,
            width=320,
            height=240,
        ),
        create_card(
            title="Разминка (5–7 минут)",
            description="Подготовьте тело:\n"
                        "1. Прыжки с разведением рук: 1 мин.\n"
                        "2. Вращения плечами и тазом: 30 сек в каждую сторону.\n"
                        "3. Динамические выпады: 10 раз на ногу.\n"
                        "4. Наклоны корпуса в стороны: 10 раз на сторону.\n"
                        "5. Поза кошки-коровы: 1 мин.",
            icon=ft.icons.DIRECTIONS_RUN,
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Скручивания",
            description="Подходы: 3 по 15–20 повторений. Отдых: 30–45 сек.\n"
                        "• Лягте на коврик, колени согнуты, руки за головой.\n"
                        "• Поднимайте плечи, напрягая пресс.\n"
                        "• Совет: не тяните шею, дышите на подъёме.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F02741101-Crunch-Floor-m_waist_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Планка",
            description="Подходы: 3 по 20–30 сек. Отдых: 30 сек.\n"
                        "• Упор лёжа на предплечьях, тело прямое.\n"
                        "• Напрягайте пресс, не прогибайтесь.\n"
                        "• Совет: дышите ровно, держите баланс.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04651101-Front-Plank_Waist_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Боковые наклоны",
            description="Подходы: 3 по 15 повторений на сторону. Отдых: 30 сек.\n"
                        "• Встаньте, бутылка в одной руке, другая на талии.\n"
                        "• Наклоняйтесь в сторону, напрягая косые мышцы.\n"
                        "• Совет: двигайтесь плавно, не округляйте спину.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04071101-Dumbbell-Side-Bend_Waist_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Приседания с прыжком",
            description="Подходы: 3 по 12–15 повторений. Отдых: 45 сек.\n"
                        "• Встаньте, ноги на ширине плеч.\n"
                        "• Приседайте, затем выпрыгивайте вверх.\n"
                        "• Совет: приземляйтесь мягко, держите колени в линии.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F15811101-Bodyweight-Rear-Lunge_Thighs-FIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Ягодичный мостик",
            description="Подходы: 3 по 15–20 повторений. Отдых: 30 сек.\n"
                        "• Лягте на коврик, колени согнуты, стопы на полу.\n"
                        "• Поднимайте таз, напрягая ягодицы.\n"
                        "• Совет: задержитесь на 1 сек вверху, не прогибайтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F10601101-Barbell-Hip-Thrust_Hips_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 1: Выпады с растяжкой",
            description="Подходы: 3 по 12 повторений на ногу. Отдых: 45 сек.\n"
                        "• Шаг вперёд, опустите колено почти до пола.\n"
                        "• Задержитесь на 5 сек, растягивая бедро.\n"
                        "• Совет: держите корпус прямым, колено над стопой.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F22181101-Dumbbell-Lunge-(female)_Thighs_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Отжимания с колен",
            description="Подходы: 3 по 10–12 повторений. Отдых: 45 сек.\n"
                        "• Упор лёжа на коленях, руки на ширине плеч.\n"
                        "• Опускайтесь, напрягая грудь и трицепсы.\n"
                        "• Совет: держите тело прямым, не прогибайтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F06621101-Push-up-m_Chest-FIX_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Разгибания с бутылкой",
            description="Подходы: 3 по 12–15 повторений. Отдых: 30 сек.\n"
                        "• Встаньте, бутылка над головой.\n"
                        "• Сгибайте локти, опуская бутылку за голову.\n"
                        "• Совет: держите локти неподвижно, работайте трицепсом.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04231101-Dumbbell-Standing-One-Arm-Extension_Upper-Arms_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Подъёмы рук с эспандером",
            description="Подходы: 3 по 12–15 повторений. Отдых: 30 сек.\n"
                        "• Встаньте на эспандер, концы в руках.\n"
                        "• Поднимайте руки через стороны до уровня плеч.\n"
                        "• Совет: не используйте инерцию, двигайтесь плавно.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F45701101-Resistance-Band-Bent-Over-Neutral-Grip-Row_Back_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Поза кошки-коровы",
            description="Подходы: 3 по 10 циклов. Отдых: 30 сек.\n"
                        "• На четвереньках, вдох: прогиб спины (корова).\n"
                        "• Выдох: округление спины (кошка).\n"
                        "• Совет: двигайтесь плавно, синхронизируйте дыхание.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F78961201-Cat-Cow-Circle-(female)_Stretching_GREEN.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Супермен с удержанием",
            description="Подходы: 3 по 15–20 сек. Отдых: 30 сек.\n"
                        "• Лягте лицом вниз, руки вытянуты вперёд.\n"
                        "• Поднимайте руки, грудь и ноги, удерживайте.\n"
                        "• Совет: напрягайте спину, дышите ровно.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F49391101-Superman-Row-(female)_Back_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 2: Растяжка спины (поза ребёнка)",
            description="Подходы: 3 по 30 сек. Отдых: 30 сек.\n"
                        "• Сядьте на пятки, вытяните руки вперёд, опустите грудь.\n"
                        "• Расслабьтесь, дышите глубоко.\n"
                        "• Совет: тянитесь вперёд, растягивая спину.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F09451101-Child-Pose_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Берпи",
            description="Подходы: 3 по 8–10 повторений. Отдых: 45 сек.\n"
                        "• Из приседа прыгните в упор лёжа, отожмитесь.\n"
                        "• Прыгните обратно и выпрыгните вверх.\n"
                        "• Совет: выполняйте в своём темпе, дышите.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F11601101-Burpee_Cardio_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Планка с касанием плеча",
            description="Подходы: 3 по 12 касаний на сторону. Отдых: 30 сек.\n"
                        "• Упор лёжа на руках, тело прямое.\n"
                        "• Поочерёдно касайтесь плеча противоположной рукой.\n"
                        "• Совет: держите баланс, не раскачивайтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F01431101-Bridge-(straight-arm)_Waist_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Приседания с боковым подъёмом ноги",
            description="Подходы: 3 по 12 повторений на сторону. Отдых: 45 сек.\n"
                        "• Приседайте, затем поднимайте ногу в сторону.\n"
                        "• Чередуйте стороны, держите равновесие.\n"
                        "• Совет: напрягайте ягодицы при подъёме ноги.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F04131101-Dumbbell-Squat_Hips_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Поза собаки мордой вниз",
            description="Подходы: 3 по 30 сек. Отдых: 30 сек.\n"
                        "• Упор лёжа, поднимите таз, формируя букву V.\n"
                        "• Вытягивайте спину, пятки тяните к полу.\n"
                        "• Совет: дышите глубоко, растягивайте спину и ноги.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F34561101-Burpee-with-Push-up-(female)_Cardio_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Растяжка бёдер (выпады)",
            description="Подходы: 3 по 30 сек на ногу. Отдых: 30 сек.\n"
                        "• Сделайте выпад, опустите заднее колено к полу.\n"
                        "• Тяните бедро, держите корпус прямым.\n"
                        "• Совет: дышите глубоко, расслабляйтесь.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F22181101-Dumbbell-Lunge-(female)_Thighs_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="День 3: Наклон к ногам",
            description="Подходы: 3 по 30 сек. Отдых: 30 сек.\n"
                        "• Сядьте, ноги вытянуты, наклоняйтесь к стопам.\n"
                        "• Тянитесь руками вперёд, растягивая спину.\n"
                        "• Совет: не округляйте спину, дышите глубоко.",
            icon=ft.icons.FITNESS_CENTER,
            img_url="https://my.lyfta.app/_next/image?url=https%3A%2F%2Fapilyfta.com%2Fstatic%2FGymvisualPNG%2F19171101-Standing-Reach-Down-Hamsting-Crossed-Legs-Stretch_Thighs_small.png&w=640&q=100",
            width=320,
            height=240,
        ),
        create_card(
            title="Заминка (5–10 минут)",
            description="Расслабьтесь и растянитесь:\n"
                        "1. Растяжка груди (руки за спиной): 1 мин.\n"
                        "2. Растяжка спины (поза ребёнка): 1 мин.\n"
                        "3. Растяжка бёдер (выпады): 30 сек на ногу.\n"
                        "4. Растяжка плеч (рука через грудь): 30 сек на сторону.\n"
                        "5. Наклон к ногам: 1 мин.\n"
                        "6. Глубокое дыхание: 1–2 мин.",
            icon=ft.icons.SELF_IMPROVEMENT,
            width=320,
            height=280,
        ),
        create_card(
            title="Питание",
            description="Для стройного тела:\n"
                        "• Дефицит калорий: –300–500 ккал (вес × 25–30 ккал).\n"
                        "• Белок: 1.6–2 г/кг (курица, рыба, яйца, творог).\n"
                        "• Углеводы: овсянка, гречка, овощи (2–3 г/кг).\n"
                        "• Жиры: орехи, авокадо, масло (0.8 г/кг).\n"
                        "• Пример дня: овсянка с ягодами, салат с курицей, рыба с брокколи.\n"
                        "• Вода: 1.5–2 л/день.",
            icon=ft.icons.RESTAURANT,
            width=320,
            height=280,
        ),
        create_card(
            title="Советы по гибкости",
            description="Улучшайте подвижность:\n"
                        "• Тренируйтесь ежедневно: 5–10 мин растяжки.\n"
                        "• Разогревайтесь: делайте динамическую растяжку перед статической.\n"
                        "• Дышите: глубокое дыхание помогает расслабиться.\n"
                        "• Прогресс: увеличивайте амплитуду каждые 2 недели.\n"
                        "• Без боли: растягивайтесь до лёгкого натяжения.",
            icon=ft.icons.PADDING_SHARP,
            width=320,
            height=240,
        ),
        create_card(
            title="Мотивация и прогресс",
            description="Двигайтесь к цели:\n"
                        "• Измерения: талия, бёдра каждые 2 недели.\n"
                        "• Фото: делайте для сравнения.\n"
                        "• Журнал: записывайте повторения и гибкость.\n"
                        "• Цели: например, коснуться пола в наклоне.\n"
                        "• Награда: новый коврик, расслабляющая ванна.",
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
        page.title = "План: Стройное тело и гибкость"
        page.bgcolor = ft.colors.BLACK
        content_area = ft.Column(expand=True)
        page.add(
            ft.Container(
                content=content_area,
                expand=True,
                padding=ft.padding.all(10),
            )
        )
        plan_body_shape(page, content_area, lambda e: None)  # Заглушка для go_back
    ft.app(target=main)