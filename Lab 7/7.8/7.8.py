import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QListWidget, QListWidgetItem, QFrame, QMessageBox)


class Transliterator:
    """Класс для транслитерации русского текста на английский"""

    # Таблица транслитерации (ГОСТ 7.79-2000, система Б)
    TRANSLIT_TABLE = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
        'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
        'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch',
        'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
        'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }

    @staticmethod
    def transliterate(text):
        """Транслитерирует русский текст на английский"""
        result = []
        i = 0
        length = len(text)

        while i < length:
            # Проверяем двухбуквенные сочетания
            if i + 1 < length:
                two_chars = text[i:i + 2].lower()
                if two_chars == 'жч':
                    result.append('zhch' if text[i].islower() else 'Zhch')
                    i += 2
                    continue

            # Проверяем трехбуквенные сочетания
            if i + 2 < length:
                three_chars = text[i:i + 3].lower()
                if three_chars == 'здч':
                    result.append('zdch' if text[i].islower() else 'Zdch')
                    i += 3
                    continue

            # Обычная транслитерация по таблице
            char = text[i]
            if char in Transliterator.TRANSLIT_TABLE:
                result.append(Transliterator.TRANSLIT_TABLE[char])
            else:
                result.append(char)  # Оставляем как есть (пробелы, цифры и т.д.)
            i += 1

        return ''.join(result)

    @staticmethod
    def split_fio(full_name):
        """Разделяет полное ФИО на отдельные компоненты"""
        parts = full_name.strip().split()

        # Стандартные случаи
        if len(parts) == 1:
            return parts[0], "", ""  # Только фамилия
        elif len(parts) == 2:
            return parts[0], parts[1], ""  # Фамилия и имя
        elif len(parts) >= 3:
            return parts[0], parts[1], parts[2]  # Фамилия, имя, отчество
        else:
            return "", "", ""


class NameTranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Переводчик ФИО (русский → английский)")
        self.setGeometry(100, 100, 600, 500)

        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Заголовок
        title_label = QLabel("Перевод ФИО с русского на английский")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Инструкция
        instruction = QLabel("Введите ФИО на русском языке (например: Иванов Иван Иванович):")
        instruction.setStyleSheet("font-size: 12px; margin: 5px;")
        main_layout.addWidget(instruction)

        # Поле для ввода
        input_layout = QHBoxLayout()
        input_label = QLabel("ФИО:")
        input_label.setFixedWidth(50)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введите фамилию, имя и отчество...")
        self.input_field.returnPressed.connect(self.translate_name)  # Enter для перевода

        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_field)
        main_layout.addLayout(input_layout)

        # Кнопки
        buttons_layout = QHBoxLayout()

        self.translate_button = QPushButton("Перевести")
        self.translate_button.setStyleSheet("font-size: 14px; padding: 8px;")
        self.translate_button.clicked.connect(self.translate_name)

        self.clear_button = QPushButton("Очистить")
        self.clear_button.setStyleSheet("font-size: 14px; padding: 8px;")
        self.clear_button.clicked.connect(self.clear_all)

        buttons_layout.addWidget(self.translate_button)
        buttons_layout.addWidget(self.clear_button)
        buttons_layout.addStretch()
        main_layout.addLayout(buttons_layout)

        # Разделитель
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator)

        # Заголовок для результатов
        results_label = QLabel("Результаты перевода:")
        results_label.setStyleSheet("font-size: 14px; font-weight: bold; margin-top: 10px;")
        main_layout.addWidget(results_label)

        # Список для отображения результатов
        self.results_list = QListWidget()
        self.results_list.setStyleSheet("font-family: 'Courier New', monospace;")
        main_layout.addWidget(self.results_list)

        # Кнопка для копирования
        copy_layout = QHBoxLayout()
        self.copy_button = QPushButton("Копировать выделенный результат")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        copy_layout.addWidget(self.copy_button)
        copy_layout.addStretch()
        main_layout.addLayout(copy_layout)

        # Статус
        self.status_label = QLabel("Готов к переводу...")
        self.status_label.setStyleSheet("color: gray; font-style: italic;")
        main_layout.addWidget(self.status_label)

        # Добавляем отступ
        main_layout.addStretch()

    def translate_name(self):
        """Выполняет перевод ФИО"""
        # Получаем введенный текст
        russian_name = self.input_field.text().strip()

        # Проверяем, что что-то введено
        if not russian_name:
            QMessageBox.warning(self, "Предупреждение", "Пожалуйста, введите ФИО для перевода.")
            return

        # Разделяем ФИО на компоненты
        last_name, first_name, middle_name = Transliterator.split_fio(russian_name)

        if not last_name:
            QMessageBox.warning(self, "Предупреждение", "Неверный формат ФИО. Введите фамилию, имя и отчество.")
            return

        # Транслитерируем каждую часть
        last_name_en = Transliterator.transliterate(last_name)
        first_name_en = Transliterator.transliterate(first_name) if first_name else ""
        middle_name_en = Transliterator.transliterate(middle_name) if middle_name else ""

        # Формируем разные варианты записи
        variants = []

        # Вариант 1: Полное ФИО
        if first_name_en and middle_name_en:
            full_name = f"{last_name_en} {first_name_en} {middle_name_en}"
            variants.append(("Полное ФИО", full_name))

        # Вариант 2: Фамилия и инициалы
        if first_name_en:
            initials = f"{first_name_en[0]}.{middle_name_en[0]}." if middle_name_en else f"{first_name_en[0]}."
            variants.append(("Фамилия с инициалами", f"{last_name_en} {initials}"))

        # Вариант 3: Имя и фамилия (западный порядок)
        if first_name_en:
            variants.append(("Имя и фамилия", f"{first_name_en} {last_name_en}"))

        # Вариант 4: Только фамилия
        variants.append(("Только фамилия", last_name_en))

        # Добавляем в список
        self.results_list.clear()

        # Добавляем оригинал
        original_item = QListWidgetItem(f"Оригинал: {russian_name}")
        original_item.setData(1, russian_name)  # Пользовательские данные
        self.results_list.addItem(original_item)

        # Добавляем разделитель
        separator_item = QListWidgetItem("─" * 50)
        separator_item.setFlags(Qt.NoItemFlags)  # Нельзя выбрать
        self.results_list.addItem(separator_item)

        # Добавляем варианты перевода
        for variant_name, variant_value in variants:
            item_text = f"{variant_name}: {variant_value}"
            item = QListWidgetItem(item_text)
            item.setData(1, variant_value)  # Сохраняем сам текст для копирования
            self.results_list.addItem(item)

        # Обновляем статус
        self.status_label.setText(f"Переведено: {russian_name}")

        # Очищаем поле ввода (опционально)
        # self.input_field.clear()

    def clear_all(self):
        """Очищает поле ввода и список результатов"""
        self.input_field.clear()
        self.results_list.clear()
        self.status_label.setText("Готов к переводу...")

    def copy_to_clipboard(self):
        """Копирует выделенный результат в буфер обмена"""
        current_item = self.results_list.currentItem()

        if not current_item:
            QMessageBox.warning(self, "Предупреждение", "Выберите результат для копирования.")
            return

        # Получаем текст из пользовательских данных
        text_to_copy = current_item.data(1)

        if not text_to_copy:
            # Если нет пользовательских данных, берем текст элемента
            text_to_copy = current_item.text()
            # Удаляем префикс "Вариант: " если есть
            if ": " in text_to_copy:
                text_to_copy = text_to_copy.split(": ", 1)[1]

        # Копируем в буфер обмена
        clipboard = QApplication.clipboard()
        clipboard.setText(text_to_copy)

        # Показываем сообщение
        self.status_label.setText(f"Скопировано: {text_to_copy[:30]}...")

        # Всплывающее сообщение
        QMessageBox.information(self, "Успех", "Текст скопирован в буфер обмена.")


def main():
    app = QApplication(sys.argv)

    # Устанавливаем стиль
    app.setStyle('Fusion')

    # Создаем и показываем окно
    window = NameTranslatorApp()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    # Импортируем Qt здесь, чтобы не загромождать код
    from PyQt5.QtCore import Qt

    main()