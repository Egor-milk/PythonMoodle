import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class UserInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Создаем элементы интерфейса
        self.name_label = QLabel('Имя:')
        self.name_input = QLineEdit()

        self.surname_label = QLabel('Фамилия:')
        self.surname_input = QLineEdit()

        self.year_label = QLabel('Год рождения:')
        self.year_input = QLineEdit()

        self.result_label = QLabel('Результат:')
        self.result_display = QLabel('')
        self.result_display.setStyleSheet("border: 1px solid gray; padding: 5px;")
        self.result_display.setMinimumHeight(30)

        self.show_button = QPushButton('Показать информацию')
        self.show_button.clicked.connect(self.display_info)

        # Размещаем элементы в layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_input)
        layout.addWidget(self.year_label)
        layout.addWidget(self.year_input)
        layout.addWidget(self.show_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)

        # Настройки окна
        self.setLayout(layout)
        self.setWindowTitle('Информация о пользователе')
        self.setGeometry(300, 300, 300, 250)

    def display_info(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        year = self.year_input.text()

        if name and surname and year:
            result_text = f"{surname}, {name}, {year}"
            self.result_display.setText(result_text)
        else:
            self.result_display.setText("Заполните все поля!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UserInfoApp()
    ex.show()
    sys.exit(app.exec_())