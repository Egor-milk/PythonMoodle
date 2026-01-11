import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.notes = {}  # {дата: заметка}
        self.colors = {}  # {дата: цвет}
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Календарь с заметками')
        self.setGeometry(100, 100, 900, 600)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Левая панель - календарь
        left_panel = QVBoxLayout()

        # Календарь
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.date_selected)
        left_panel.addWidget(self.calendar)

        # Информация о дате
        self.date_info = QLabel()
        self.date_info.setStyleSheet("font-size: 14px; padding: 10px;")
        left_panel.addWidget(self.date_info)

        # Правая панель - заметки
        right_panel = QVBoxLayout()

        # Поле поиска
        search_layout = QHBoxLayout()
        search_label = QLabel("Поиск заметки:")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Введите текст для поиска...")
        search_button = QPushButton("Найти")
        search_button.clicked.connect(self.search_notes)
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)
        right_panel.addLayout(search_layout)

        # Выбор диапазона дат
        range_layout = QHBoxLayout()
        range_label = QLabel("Диапазон:")
        self.date_from = QDateEdit()
        self.date_from.setDate(QDate.currentDate())
        self.date_to = QDateEdit()
        self.date_to.setDate(QDate.currentDate().addDays(7))
        range_button = QPushButton("Показать заметки")
        range_button.clicked.connect(self.show_range_notes)
        range_layout.addWidget(range_label)
        range_layout.addWidget(self.date_from)
        range_layout.addWidget(QLabel("до"))
        range_layout.addWidget(self.date_to)
        range_layout.addWidget(range_button)
        right_panel.addLayout(range_layout)

        # Операции с датами
        date_ops_layout = QHBoxLayout()
        self.n_days_input = QSpinBox()
        self.n_days_input.setRange(1, 365)
        self.n_days_input.setValue(7)

        date_ops_layout.addWidget(QLabel("N дней:"))
        date_ops_layout.addWidget(self.n_days_input)

        calc_future_btn = QPushButton("Текущая + N")
        calc_future_btn.clicked.connect(self.calc_future_date)
        date_ops_layout.addWidget(calc_future_btn)

        calc_past_btn = QPushButton("Текущая - N")
        calc_past_btn.clicked.connect(self.calc_past_date)
        date_ops_layout.addWidget(calc_past_btn)

        right_panel.addLayout(date_ops_layout)

        # Поле для заметки
        right_panel.addWidget(QLabel("Заметка для выбранной даты:"))
        self.note_text = QTextEdit()
        self.note_text.setMaximumHeight(100)
        right_panel.addWidget(self.note_text)

        # Кнопки для заметки
        note_buttons = QHBoxLayout()
        save_note_btn = QPushButton("Сохранить заметку")
        save_note_btn.clicked.connect(self.save_note)
        clear_note_btn = QPushButton("Очистить")
        clear_note_btn.clicked.connect(self.clear_note)
        note_buttons.addWidget(save_note_btn)
        note_buttons.addWidget(clear_note_btn)
        right_panel.addLayout(note_buttons)

        # Выбор цвета
        color_layout = QHBoxLayout()
        color_layout.addWidget(QLabel("Цвет фона:"))

        self.color_combo = QComboBox()
        self.color_combo.addItems([
            "Без цвета", "Красный", "Зеленый", "Синий",
            "Желтый", "Фиолетовый", "Оранжевый", "Серый"
        ])
        color_layout.addWidget(self.color_combo)

        set_color_btn = QPushButton("Установить цвет")
        set_color_btn.clicked.connect(self.set_date_color)
        color_layout.addWidget(set_color_btn)

        right_panel.addLayout(color_layout)

        # Список заметок
        right_panel.addWidget(QLabel("Все заметки:"))
        self.notes_list = QListWidget()
        right_panel.addWidget(self.notes_list)

        # Добавляем панели в главный layout
        main_layout.addLayout(left_panel, 2)
        main_layout.addLayout(right_panel, 1)

        # Устанавливаем текущую дату
        self.update_date_info()

    def date_selected(self):
        selected_date = self.calendar.selectedDate()
        self.update_date_info()

        # Загружаем заметку для выбранной даты
        date_str = selected_date.toString("yyyy-MM-dd")
        self.note_text.setText(self.notes.get(date_str, ""))

        # Устанавливаем цвет в комбобокс
        current_color = self.colors.get(date_str)
        if current_color:
            for i in range(self.color_combo.count()):
                if self.color_combo.itemText(i) == current_color:
                    self.color_combo.setCurrentIndex(i)
                    break
        else:
            self.color_combo.setCurrentIndex(0)

    def update_date_info(self):
        selected_date = self.calendar.selectedDate()
        current_date = QDate.currentDate()

        info_text = f"""
        Выбранная дата: {selected_date.toString('dd.MM.yyyy')}
        День недели: {self.get_russian_weekday(selected_date.dayOfWeek())}
        Текущая дата: {current_date.toString('dd.MM.yyyy')}
        День недели: {self.get_russian_weekday(current_date.dayOfWeek())}
        """

        self.date_info.setText(info_text)

    def get_russian_weekday(self, weekday):
        days = {
            1: "Понедельник",
            2: "Вторник",
            3: "Среда",
            4: "Четверг",
            5: "Пятница",
            6: "Суббота",
            7: "Воскресенье"
        }
        return days.get(weekday, "")

    def save_note(self):
        selected_date = self.calendar.selectedDate()
        date_str = selected_date.toString("yyyy-MM-dd")
        note = self.note_text.toPlainText()

        if note.strip():
            self.notes[date_str] = note
            QMessageBox.information(self, "Успех", "Заметка сохранена!")
            self.update_notes_list()
        else:
            # Если заметка пустая, удаляем её
            if date_str in self.notes:
                del self.notes[date_str]
                self.update_notes_list()

    def clear_note(self):
        self.note_text.clear()

    def set_date_color(self):
        selected_date = self.calendar.selectedDate()
        date_str = selected_date.toString("yyyy-MM-dd")
        color_name = self.color_combo.currentText()

        if color_name == "Без цвета":
            if date_str in self.colors:
                del self.colors[date_str]
        else:
            self.colors[date_str] = color_name

        self.update_calendar_colors()

    def update_calendar_colors(self):
        # Очищаем все форматы
        self.calendar.setDateTextFormat(QDate(), QTextCharFormat())

        # Устанавливаем цвета для дат
        color_map = {
            "Красный": Qt.red,
            "Зеленый": Qt.green,
            "Синий": Qt.blue,
            "Желтый": Qt.yellow,
            "Фиолетовый": Qt.magenta,
            "Оранжевый": QColor(255, 165, 0),
            "Серый": Qt.gray
        }

        for date_str, color_name in self.colors.items():
            if color_name in color_map:
                date = QDate.fromString(date_str, "yyyy-MM-dd")
                fmt = QTextCharFormat()
                fmt.setBackground(color_map[color_name])
                self.calendar.setDateTextFormat(date, fmt)

        # Подсвечиваем даты с заметками
        fmt = QTextCharFormat()
        fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(Qt.darkBlue)

        for date_str in self.notes:
            if date_str not in self.colors:  # Не перезаписываем уже раскрашенные
                date = QDate.fromString(date_str, "yyyy-MM-dd")
                self.calendar.setDateTextFormat(date, fmt)

    def search_notes(self):
        search_text = self.search_input.text().lower()
        if not search_text:
            return

        self.notes_list.clear()
        found_dates = []

        for date_str, note in self.notes.items():
            if search_text in note.lower():
                found_dates.append((date_str, note))

        if found_dates:
            for date_str, note in found_dates:
                date = QDate.fromString(date_str, "yyyy-MM-dd")
                item_text = f"{date.toString('dd.MM.yyyy')}: {note[:50]}..."
                self.notes_list.addItem(item_text)
        else:
            self.notes_list.addItem("Заметки не найдены")

    def show_range_notes(self):
        date_from = self.date_from.date()
        date_to = self.date_to.date()

        self.notes_list.clear()

        for date_str, note in sorted(self.notes.items()):
            date = QDate.fromString(date_str, "yyyy-MM-dd")
            if date_from <= date <= date_to:
                item_text = f"{date.toString('dd.MM.yyyy')}: {note[:50]}..."
                self.notes_list.addItem(item_text)

    def calc_future_date(self):
        n_days = self.n_days_input.value()
        current_date = QDate.currentDate()
        future_date = current_date.addDays(n_days)

        QMessageBox.information(
            self,
            "Результат",
            f"Текущая дата + {n_days} дней = {future_date.toString('dd.MM.yyyy')}\n"
            f"День недели: {self.get_russian_weekday(future_date.dayOfWeek())}"
        )

    def calc_past_date(self):
        n_days = self.n_days_input.value()
        current_date = QDate.currentDate()
        past_date = current_date.addDays(-n_days)

        QMessageBox.information(
            self,
            "Результат",
            f"Текущая дата - {n_days} дней = {past_date.toString('dd.MM.yyyy')}\n"
            f"День недели: {self.get_russian_weekday(past_date.dayOfWeek())}"
        )

    def update_notes_list(self):
        self.notes_list.clear()
        for date_str, note in sorted(self.notes.items()):
            date = QDate.fromString(date_str, "yyyy-MM-dd")
            item_text = f"{date.toString('dd.MM.yyyy')}: {note[:50]}..."
            self.notes_list.addItem(item_text)

        self.update_calendar_colors()


def main():
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()