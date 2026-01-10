import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QMessageBox, QFrame, QGridLayout)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход в систему")
        self.setGeometry(300, 200, 400, 350)

        # Устанавливаем иконку приложения
        try:
            self.setWindowIcon(QIcon("icon.png"))
        except:
            pass  # Если иконки нет, пропускаем

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # Заголовок
        title_label = QLabel("Вход в систему")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        main_layout.addWidget(title_label)

        # Иконка пользователя (заглушка текстом)
        user_icon_label = QLabel("👤")
        user_icon_label.setAlignment(Qt.AlignCenter)
        user_icon_label.setFont(QFont("Arial", 40))
        user_icon_label.setStyleSheet("margin-bottom: 20px;")
        main_layout.addWidget(user_icon_label)

        # Форма входа
        form_widget = QWidget()
        form_layout = QGridLayout(form_widget)
        form_layout.setVerticalSpacing(15)

        # Поле для логина
        login_label = QLabel("Логин:")
        login_label.setFont(QFont("Arial", 10))

        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Введите ваш логин")
        self.login_input.setMinimumHeight(35)
        self.login_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
        """)

        # Поле для пароля
        password_label = QLabel("Пароль:")
        password_label.setFont(QFont("Arial", 10))

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите ваш пароль")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(35)
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
        """)

        # Кнопка показать/скрыть пароль
        self.show_password_btn = QPushButton("👁")
        self.show_password_btn.setFixedSize(30, 35)
        self.show_password_btn.setStyleSheet("""
            QPushButton {
                border: 1px solid #bdc3c7;
                border-left: none;
                border-radius: 0 4px 4px 0;
                background-color: #ecf0f1;
            }
            QPushButton:hover {
                background-color: #d5dbdb;
            }
        """)
        self.show_password_btn.clicked.connect(self.toggle_password_visibility)

        # Контейнер для пароля с кнопкой
        password_container = QWidget()
        password_layout = QHBoxLayout(password_container)
        password_layout.setContentsMargins(0, 0, 0, 0)
        password_layout.addWidget(self.password_input)
        password_layout.addWidget(self.show_password_btn)

        # Добавляем элементы в форму
        form_layout.addWidget(login_label, 0, 0)
        form_layout.addWidget(self.login_input, 0, 1)
        form_layout.addWidget(password_label, 1, 0)
        form_layout.addWidget(password_container, 1, 1)

        main_layout.addWidget(form_widget)

        # Кнопки
        buttons_widget = QWidget()
        buttons_layout = QVBoxLayout(buttons_widget)
        buttons_layout.setSpacing(10)

        # Кнопка входа
        self.login_button = QPushButton("Войти")
        self.login_button.setMinimumHeight(40)
        self.login_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c6ea4;
            }
            QPushButton:disabled {
                background-color: #bdc3c7;
            }
        """)
        self.login_button.clicked.connect(self.attempt_login)

        # Кнопка отмены
        self.cancel_button = QPushButton("Отмена")
        self.cancel_button.setMinimumHeight(35)
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        self.cancel_button.clicked.connect(self.close)

        buttons_layout.addWidget(self.login_button)
        buttons_layout.addWidget(self.cancel_button)
        main_layout.addWidget(buttons_widget)

        # Сообщение о попытках
        self.attempts_label = QLabel("")
        self.attempts_label.setAlignment(Qt.AlignCenter)
        self.attempts_label.setStyleSheet("color: #e74c3c; font-weight: bold;")
        main_layout.addWidget(self.attempts_label)

        # Статусная строка внизу
        status_widget = QWidget()
        status_layout = QHBoxLayout(status_widget)

        self.status_label = QLabel("Готов к входу")
        self.status_label.setStyleSheet("color: #7f8c8d; font-size: 11px;")

        version_label = QLabel("v1.0")
        version_label.setStyleSheet("color: #7f8c8d; font-size: 11px;")

        status_layout.addWidget(self.status_label)
        status_layout.addStretch()
        status_layout.addWidget(version_label)

        main_layout.addWidget(status_widget)

        # Переменные для системы безопасности
        self.login_attempts = 0
        self.max_attempts = 3
        self.locked_until = None

        # Список пользователей (в реальном приложении это должно быть в БД)
        self.users = {
            "admin": {"password": "admin123", "name": "Администратор"},
            "egor": {"password": "1", "name": "egor"},
            "ivanov": {"password": "qwerty", "name": "Иванов Иван"}
        }

        # Таймер для разблокировки
        self.unlock_timer = QTimer()
        self.unlock_timer.timeout.connect(self.check_unlock)

        # Разрешаем ввод по Enter
        self.password_input.returnPressed.connect(self.attempt_login)

    def toggle_password_visibility(self):
        """Показывает или скрывает пароль"""
        if self.password_input.echoMode() == QLineEdit.Password:
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.show_password_btn.setText("🙈")
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.show_password_btn.setText("👁")

    def check_unlock(self):
        """Проверяет, можно ли разблокировать вход"""
        from datetime import datetime
        if self.locked_until and datetime.now() >= self.locked_until:
            self.enable_login()
            self.locked_until = None
            self.unlock_timer.stop()

    def enable_login(self):
        """Включает поля ввода и кнопку"""
        self.login_input.setEnabled(True)
        self.password_input.setEnabled(True)
        self.login_button.setEnabled(True)
        self.status_label.setText("Готов к входу")
        self.attempts_label.setText("")

    def disable_login(self, message):
        """Отключает поля ввода и кнопку"""
        self.login_input.setEnabled(False)
        self.password_input.setEnabled(False)
        self.login_button.setEnabled(False)
        self.status_label.setText(message)
        self.attempts_label.setText("")

    def attempt_login(self):
        """Попытка входа в систему"""
        login = self.login_input.text().strip()
        password = self.password_input.text()

        # Проверка на пустые поля
        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля!")
            return

        # Проверка блокировки
        if self.locked_until:
            from datetime import datetime
            remaining = (self.locked_until - datetime.now()).seconds
            minutes = remaining // 60
            seconds = remaining % 60
            QMessageBox.warning(self, "Система заблокирована",
                                f"Попробуйте через {minutes}:{seconds:02d}")
            return

        # Проверка учетных данных
        if login in self.users and self.users[login]["password"] == password:
            self.successful_login(login)
        else:
            self.failed_login()

    def successful_login(self, login):
        """Успешный вход"""
        user_name = self.users[login]["name"]

        # Сбрасываем счетчик попыток
        self.login_attempts = 0

        # Показываем сообщение об успехе
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Успешный вход")
        msg_box.setText(f"Добро пожаловать, {user_name}!")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.button(QMessageBox.Ok).setText("Продолжить")
        msg_box.exec_()

        # В реальном приложении здесь был бы переход к основному окну
        self.status_label.setText(f"Вход выполнен: {user_name}")

        # Очищаем поля (в демо-версии)
        self.password_input.clear()

        # Пример: закрываем окно входа (в реальном приложении открываем главное окно)
        QMessageBox.information(self, "Демо-версия",
                                "В реальном приложении здесь открывалось бы основное окно программы.\n\n"
                                f"Пользователь: {user_name}\n"
                                "Вход выполнен успешно!")
        self.close()

    def failed_login(self):
        """Неудачная попытка входа"""
        self.login_attempts += 1
        remaining_attempts = self.max_attempts - self.login_attempts

        if remaining_attempts > 0:
            # Показываем предупреждение
            self.attempts_label.setText(f"Неверный логин или пароль. Осталось попыток: {remaining_attempts}")
            self.status_label.setText("Ошибка входа")

            # Анимация ошибки
            self.login_button.setStyleSheet("""
                QPushButton {
                    background-color: #e74c3c;
                    color: white;
                    border: none;
                    border-radius: 4px;
                }
            """)

            QTimer.singleShot(300, lambda: self.login_button.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """))

            # Очищаем поле пароля
            self.password_input.clear()
            self.password_input.setFocus()

        else:
            # Блокируем систему
            self.lock_system()

    def lock_system(self):
        """Блокирует систему на время"""
        from datetime import datetime, timedelta

        # Устанавливаем блокировку на 30 секунд (в реальности можно на несколько минут)
        lock_time = 30  # секунд
        self.locked_until = datetime.now() + timedelta(seconds=lock_time)

        # Отключаем вход
        self.disable_login(f"Система заблокирована на {lock_time} секунд")
        self.attempts_label.setText("Слишком много неудачных попыток!")

        # Запускаем таймер для проверки разблокировки
        self.unlock_timer.start(1000)  # Проверка каждую секунду

        # Показываем сообщение
        QMessageBox.critical(self, "Доступ заблокирован",
                             f"Слишком много неудачных попыток входа.\n"
                             f"Попробуйте через {lock_time} секунд.")

    def closeEvent(self, event):
        """Обработчик закрытия окна"""
        if self.login_attempts > 0:
            reply = QMessageBox.question(
                self, "Подтверждение",
                "Вы действительно хотите выйти?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()


def main():
    app = QApplication(sys.argv)

    # Устанавливаем стиль приложения
    app.setStyle('Fusion')

    # Настройки для темной темы (опционально)
    palette = app.palette()
    palette.setColor(palette.Window, QColor(240, 240, 240))
    palette.setColor(palette.WindowText, QColor(0, 0, 0))
    app.setPalette(palette)

    # Создаем и показываем окно входа
    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    # Импортируем QColor для настройки палитры
    from PyQt5.QtGui import QColor

    main()