import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QGroupBox, QRadioButton, QTextEdit,
                             QLabel, QFrame)


class ZodiacApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Знаки Зодиака")
        self.setGeometry(100, 100, 500, 500)

        # Создаем центральный виджет и основной макет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Заголовок программы
        title_label = QLabel("Выберите знак зодиака:")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        main_layout.addWidget(title_label)

        # Панель с переключателями
        zodiac_panel = QWidget()
        zodiac_layout = QHBoxLayout(zodiac_panel)

        # Левая колонка знаков
        left_column = QWidget()
        left_layout = QVBoxLayout(left_column)

        # Правая колонка знаков
        right_column = QWidget()
        right_layout = QVBoxLayout(right_column)

        # Список знаков зодиака
        zodiac_signs = [
            "Овен", "Телец", "Близнецы", "Рак",
            "Лев", "Дева", "Весы", "Скорпион",
            "Стрелец", "Козерог", "Водолей", "Рыбы"
        ]

        # Создаем переключатели для каждого знака
        self.radio_buttons = []
        half = len(zodiac_signs) // 2

        # Распределяем знаки по двум колонкам
        for i, sign in enumerate(zodiac_signs):
            radio = QRadioButton(sign)
            radio.toggled.connect(self.on_zodiac_selected)
            self.radio_buttons.append(radio)

            if i < half:
                left_layout.addWidget(radio)
            else:
                right_layout.addWidget(radio)

        # Добавляем отступы в конце колонок
        left_layout.addStretch()
        right_layout.addStretch()

        # Добавляем колонки в панель
        zodiac_layout.addWidget(left_column)
        zodiac_layout.addWidget(right_column)

        # Добавляем панель с переключателями в основной макет
        main_layout.addWidget(zodiac_panel)

        # Разделитель
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator)

        # Заголовок для поля с описанием
        description_label = QLabel("Описание знака:")
        description_label.setStyleSheet("font-size: 14px; font-weight: bold; margin-top: 10px;")
        main_layout.addWidget(description_label)

        # Текстовое поле для отображения описания
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setPlaceholderText("Выберите знак зодиака для отображения описания")
        self.text_edit.setMinimumHeight(200)
        main_layout.addWidget(self.text_edit)

        # Добавляем отступ в конце
        main_layout.addStretch()

        # Словарь с описаниями знаков зодиака
        self.zodiac_descriptions = {
            "Овен": "Овен (21 марта - 19 апреля) - первый знак зодиака.\n"
                    "Стихия: Огонь\nПланета-покровитель: Марс\n\n"
                    "Представители этого знака энергичны, решительны и инициативны. "
                    "Они часто становятся лидерами и не боятся трудностей.",

            "Телец": "Телец (20 апреля - 20 мая) - второй знак зодиака.\n"
                     "Стихия: Земля\nПланета-покровитель: Венера\n\n"
                     "Телец практичен, надежен и ценит комфорт. "
                     "Это верные друзья и партнеры, которые ценят стабильность.",

            "Близнецы": "Близнецы (21 мая - 21 июня) - третий знак зодиака.\n"
                        "Стихия: Воздух\nПланета-покровитель: Меркурий\n\n"
                        "Близнецы общительны, любознательны и адаптивны. "
                        "Они легко находят общий язык с разными людьми.",

            "Рак": "Рак (22 июня - 22 июля) - четвертый знак зодиака.\n"
                   "Стихия: Вода\nПланета-покровитель: Луна\n\n"
                   "Рак эмоционален, заботлив и интуитивен. "
                   "Это преданные семьянины, которые ценят домашний уют.",

            "Лев": "Лев (23 июля - 22 августа) - пятый знак зодиака.\n"
                   "Стихия: Огонь\nПланета-покровитель: Солнце\n\n"
                   "Лев уверен в себе, щедр и творчески одарен. "
                   "Они любят быть в центре внимания и часто достигают успеха.",

            "Дева": "Дева (23 августа - 22 сентября) - шестой знак зодиака.\n"
                    "Стихия: Земля\nПланета-покровитель: Меркурий\n\n"
                    "Дева практична, внимательна к деталям и аналитична. "
                    "Они стремятся к совершенству во всем.",

            "Весы": "Весы (23 сентября - 23 октября) - седьмой знак зодиака.\n"
                    "Стихия: Воздух\nПланета-покровитель: Венера\n\n"
                    "Весы стремятся к гармонии, справедливы и дипломатичны. "
                    "Они избегают конфликтов и ищут компромиссы.",

            "Скорпион": "Скорпион (24 октября - 22 ноября) - восьмой знак зодиака.\n"
                        "Стихия: Вода\nПланета-покровитель: Плутон\n\n"
                        "Скорпион страстен, решительный и проницателен. "
                        "Они обладают сильной волей и никогда не сдаются.",

            "Стрелец": "Стрелец (23 ноября - 21 декабря) - девятый знак зодиака.\n"
                       "Стихия: Огонь\nПланета-покровитель: Юпитер\n\n"
                       "Стрелец оптимистичен, любит свободу и приключения. "
                       "Они постоянно стремятся к новым знаниям и впечатлениям.",

            "Козерог": "Козерог (22 декабря - 19 января) - десятый знак зодиака.\n"
                       "Стихия: Земля\nПланета-покровитель: Сатурн\n\n"
                       "Козерог амбициозен, дисциплинирован и ответственен. "
                       "Они упорно работают для достижения своих целей.",

            "Водолей": "Водолей (20 января - 18 февраля) - одиннадцатый знак зодиака.\n"
                       "Стихия: Воздух\nПланета-покровитель: Уран\n\n"
                       "Водолей оригинален, независим и гуманистичен. "
                       "Они часто имеют нестандартное мышление и идут своим путем.",

            "Рыбы": "Рыбы (19 февраля - 20 марта) - двенадцатый знак зодиака.\n"
                    "Стихия: Вода\nПланета-покровитель: Нептун\n\n"
                    "Рыбы чувствительны, сострадательны и обладают развитой интуицией. "
                    "Они творческие натуры с богатым внутренним миром."
        }

    def on_zodiac_selected(self):
        """Обработчик выбора знака зодиака"""
        # Находим выбранный переключатель
        for radio in self.radio_buttons:
            if radio.isChecked():
                sign = radio.text()
                # Отображаем описание выбранного знака
                self.text_edit.setText(self.zodiac_descriptions.get(sign, "Описание не найдено"))
                break


def main():
    app = QApplication(sys.argv)
    window = ZodiacApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()