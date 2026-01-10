import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QGroupBox, QRadioButton, QCheckBox,
                             QPushButton, QTextEdit, QLabel, QFrame)


class PersonalityApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Характеристика личности")
        self.setGeometry(100, 100, 500, 550)

        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Заголовок
        title_label = QLabel("Выберите характеристики, которые описывают вас:")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        main_layout.addWidget(title_label)

        # Группа для выбора пола (переключатели)
        gender_group = QGroupBox("Пол")
        gender_layout = QVBoxLayout()

        self.male_radio = QRadioButton("Мужчина")
        self.female_radio = QRadioButton("Женщина")

        # По умолчанию ничего не выбрано
        self.male_radio.setAutoExclusive(True)
        self.female_radio.setAutoExclusive(True)

        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        gender_group.setLayout(gender_layout)
        main_layout.addWidget(gender_group)

        # Снимаем выделение при повторном клике
        self.male_radio.clicked.connect(lambda: self.uncheck_if_checked(self.male_radio, self.female_radio))
        self.female_radio.clicked.connect(lambda: self.uncheck_if_checked(self.female_radio, self.male_radio))

        # Группа для качеств (флажки)
        qualities_group = QGroupBox("Качества личности")
        qualities_layout = QVBoxLayout()

        # Создаем флажки для качеств
        self.smart_check = QCheckBox("Умный")
        self.initiative_check = QCheckBox("Инициативный")
        self.friendly_check = QCheckBox("Дружелюбный")
        self.hardworking_check = QCheckBox("Трудолюбивый")

        qualities_layout.addWidget(self.smart_check)
        qualities_layout.addWidget(self.initiative_check)
        qualities_layout.addWidget(self.friendly_check)
        qualities_layout.addWidget(self.hardworking_check)
        qualities_group.setLayout(qualities_layout)
        main_layout.addWidget(qualities_group)

        # Кнопка для получения характеристики
        self.characterize_button = QPushButton("Дать характеристику")
        self.characterize_button.setStyleSheet("font-size: 14px; padding: 8px;")
        self.characterize_button.clicked.connect(self.generate_characteristic)
        main_layout.addWidget(self.characterize_button)

        # Разделитель
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator)

        # Поле для вывода характеристики
        result_label = QLabel("Ваша характеристика:")
        result_label.setStyleSheet("font-size: 14px; font-weight: bold; margin-top: 10px;")
        main_layout.addWidget(result_label)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText("Здесь появится ваша характеристика...")
        self.result_text.setMinimumHeight(150)
        main_layout.addWidget(self.result_text)

        # Добавляем отступ в конце
        main_layout.addStretch()

    def uncheck_if_checked(self, clicked_radio, other_radio):
        """Снимает выделение с радиокнопки, если она уже была выделена"""
        if clicked_radio.isChecked():
            # Если кнопка уже была нажата, снимаем выделение
            clicked_radio.setChecked(False)
        else:
            # Если кнопка не была нажата, выделяем ее и снимаем выделение с другой
            clicked_radio.setChecked(True)
            other_radio.setChecked(False)

    def generate_characteristic(self):
        """Генерирует характеристику на основе выбранных параметров"""
        characteristics = []

        # Определяем пол
        if self.male_radio.isChecked():
            characteristics.append("Мужчина")
        elif self.female_radio.isChecked():
            characteristics.append("Женщина")
        else:
            characteristics.append("Пол не указан")

        # Собираем выбранные качества
        qualities = []
        if self.smart_check.isChecked():
            qualities.append("умный")
        if self.initiative_check.isChecked():
            qualities.append("инициативный")
        if self.friendly_check.isChecked():
            qualities.append("дружелюбный")
        if self.hardworking_check.isChecked():
            qualities.append("трудолюбивый")

        # Формируем характеристику
        if qualities:
            if len(qualities) == 1:
                qualities_str = qualities[0]
            elif len(qualities) == 2:
                qualities_str = f"{qualities[0]} и {qualities[1]}"
            else:
                qualities_str = ", ".join(qualities[:-1]) + f" и {qualities[-1]}"

            characteristic = f"Вы - {characteristics[0].lower()}. "
            characteristic += f"Вы обладаете такими качествами, как {qualities_str}."
        else:
            characteristic = f"Вы - {characteristics[0].lower()}. "
            characteristic += "Качества личности не выбраны."

        # Добавляем дополнительную оценку в зависимости от количества выбранных качеств
        num_qualities = len(qualities)
        if num_qualities > 0:
            characteristic += f"\n\n"

            if num_qualities == 4:
                characteristic += "Отличный выбор! Вы выбрали все качества, что говорит о разносторонней личности."
            elif num_qualities == 3:
                characteristic += "Хороший набор качеств! Вы уверены в себе и знаете свои сильные стороны."
            elif num_qualities == 2:
                characteristic += "Неплохой выбор. У вас есть четкое представление о своих главных качествах."
            elif num_qualities == 1:
                characteristic += "Интересный выбор. Вы выделили для себя самое важное качество."
        else:
            characteristic += "\n\nПопробуйте выбрать хотя бы одно качество, чтобы получить более подробную характеристику."

        # Выводим результат
        self.result_text.setText(characteristic)


def main():
    app = QApplication(sys.argv)
    window = PersonalityApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()