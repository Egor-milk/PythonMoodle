import sys
import json
import hashlib
import os
from datetime import datetime, date
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QMessageBox, QTableWidget, QTableWidgetItem,
                             QTabWidget, QFrame, QComboBox, QDateEdit,
                             QDoubleSpinBox, QTextEdit, QListWidget,
                             QListWidgetItem, QInputDialog, QDialog,
                             QGridLayout, QGroupBox, QHeaderView)
from PyQt5.QtCore import Qt, QDate, QTimer
from PyQt5.QtGui import QFont, QIcon, QColor


class LoginWindow(QDialog):
    """Окно авторизации и регистрации"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление финансами - Вход")
        self.setFixedSize(800, 350)

        self.users_file = "users.json"
        self.load_users()

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Заголовок
        title = QLabel("Управление личными финансами")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Поле логина
        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Введите логин")
        self.login_input.setMinimumHeight(35)
        layout.addWidget(self.login_input)

        # Поле пароля
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(35)
        layout.addWidget(self.password_input)

        # Кнопки
        btn_layout = QHBoxLayout()

        self.login_btn = QPushButton("Войти")
        self.login_btn.setMinimumHeight(40)
        self.login_btn.clicked.connect(self.login)

        self.register_btn = QPushButton("Регистрация")
        self.register_btn.setMinimumHeight(40)
        self.register_btn.clicked.connect(self.show_register)

        btn_layout.addWidget(self.login_btn)
        btn_layout.addWidget(self.register_btn)
        layout.addLayout(btn_layout)

        # Статус
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def load_users(self):
        """Загрузка пользователей из файла"""
        try:
            if os.path.exists(self.users_file):
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    self.users = json.load(f)
            else:
                self.users = {}
        except:
            self.users = {}

    def save_users(self):
        """Сохранение пользователей в файл"""
        try:
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump(self.users, f, ensure_ascii=False, indent=2)
            return True
        except:
            return False

    def hash_password(self, password):
        """Хеширование пароля"""
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        """Авторизация пользователя"""
        login = self.login_input.text().strip()
        password = self.password_input.text()

        if not login or not password:
            self.status_label.setText("Заполните все поля")
            self.status_label.setStyleSheet("color: red;")
            return

        if login in self.users:
            hashed_password = self.hash_password(password)
            if self.users[login]['password'] == hashed_password:
                self.current_user = login
                self.accept()  # Успешный вход
            else:
                self.status_label.setText("Неверный пароль")
                self.status_label.setStyleSheet("color: red;")
        else:
            self.status_label.setText("Пользователь не найден")
            self.status_label.setStyleSheet("color: red;")

    def show_register(self):
        """Показать окно регистрации"""
        dialog = RegisterDialog(self)
        if dialog.exec_():
            self.load_users()
            self.status_label.setText("Регистрация успешна! Теперь войдите.")
            self.status_label.setStyleSheet("color: green;")


class RegisterDialog(QDialog):
    """Диалог регистрации"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Регистрация")
        self.setFixedSize(400, 450)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)

        title = QLabel("Регистрация нового пользователя")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Поля для регистрации
        fields = [
            ("Логин:", QLineEdit()),
            ("Пароль:", QLineEdit(), True),
            ("Подтверждение пароля:", QLineEdit(), True),
            ("Имя:", QLineEdit()),
            ("Email:", QLineEdit()),
            ("Телефон:", QLineEdit()),
        ]

        self.inputs = {}
        for label_text, input_widget, *is_password in fields:
            layout.addWidget(QLabel(label_text))
            if is_password:
                input_widget.setEchoMode(QLineEdit.Password)
            input_widget.setMinimumHeight(30)
            layout.addWidget(input_widget)
            self.inputs[label_text] = input_widget

        # Кнопки
        btn_layout = QHBoxLayout()
        register_btn = QPushButton("Зарегистрироваться")
        register_btn.clicked.connect(self.register)
        cancel_btn = QPushButton("Отмена")
        cancel_btn.clicked.connect(self.reject)

        btn_layout.addWidget(register_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

        self.status_label = QLabel("")
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def register(self):
        """Регистрация нового пользователя"""
        login = self.inputs["Логин:"].text().strip()
        password = self.inputs["Пароль:"].text()
        confirm_password = self.inputs["Подтверждение пароля:"].text()
        name = self.inputs["Имя:"].text().strip()
        email = self.inputs["Email:"].text().strip()
        phone = self.inputs["Телефон:"].text().strip()

        # Валидация
        if not all([login, password, name]):
            self.status_label.setText("Заполните обязательные поля")
            self.status_label.setStyleSheet("color: red;")
            return

        if password != confirm_password:
            self.status_label.setText("Пароли не совпадают")
            self.status_label.setStyleSheet("color: red;")
            return

        if len(password) < 6:
            self.status_label.setText("Пароль должен быть не менее 6 символов")
            self.status_label.setStyleSheet("color: red;")
            return

        # Загрузка существующих пользователей
        try:
            if os.path.exists("users.json"):
                with open("users.json", 'r', encoding='utf-8') as f:
                    users = json.load(f)
            else:
                users = {}
        except:
            users = {}

        # Проверка существования пользователя
        if login in users:
            self.status_label.setText("Пользователь уже существует")
            self.status_label.setStyleSheet("color: red;")
            return

        # Хеширование пароля
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Создание пользователя
        users[login] = {
            'password': hashed_password,
            'name': name,
            'email': email,
            'phone': phone,
            'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'personal_data': {
                'address': '',
                'birth_date': '',
                'notes': ''
            },
            'categories': {
                'income': ['Зарплата', 'Фриланс', 'Инвестиции', 'Подарки'],
                'expense': ['Продукты', 'Транспорт', 'Жилье', 'Развлечения', 'Здоровье']
            }
        }

        # Сохранение
        try:
            with open("users.json", 'w', encoding='utf-8') as f:
                json.dump(users, f, ensure_ascii=False, indent=2)

            # Создание файла данных пользователя
            user_data = {
                'transactions': [],
                'income_sources': [],
                'settings': {}
            }

            with open(f"data_{login}.json", 'w', encoding='utf-8') as f:
                json.dump(user_data, f, ensure_ascii=False, indent=2)

            self.status_label.setText("Регистрация успешна!")
            self.status_label.setStyleSheet("color: green;")
            QTimer.singleShot(1000, self.accept)

        except Exception as e:
            self.status_label.setText(f"Ошибка сохранения: {str(e)}")
            self.status_label.setStyleSheet("color: red;")


class PersonalDataTab(QWidget):
    """Вкладка для управления личными данными"""

    def __init__(self, user_data, username):
        super().__init__()
        self.user_data = user_data
        self.username = username
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Заголовок
        title = QLabel("Личные данные")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title)

        # Форма для ввода данных
        form_group = QGroupBox("Основная информация")
        form_layout = QGridLayout()

        self.fields = {}
        fields_config = [
            ("ФИО:", QLineEdit(), 0, 0),
            ("Дата рождения:", QDateEdit(), 0, 1),
            ("Адрес:", QLineEdit(), 1, 0),
            ("Город:", QLineEdit(), 1, 1),
            ("Email:", QLineEdit(), 2, 0),
            ("Телефон:", QLineEdit(), 2, 1),
            ("Место работы:", QLineEdit(), 3, 0),
            ("Должность:", QLineEdit(), 3, 1)
        ]

        for label, widget, row, col in fields_config:
            form_layout.addWidget(QLabel(label), row, col * 2)
            if isinstance(widget, QDateEdit):
                widget.setCalendarPopup(True)
                widget.setDisplayFormat("dd.MM.yyyy")
                widget.setDate(QDate.currentDate())
            widget.setMinimumHeight(30)
            form_layout.addWidget(widget, row, col * 2 + 1)
            self.fields[label] = widget

        form_group.setLayout(form_layout)
        layout.addWidget(form_group)

        # Дополнительные заметки
        notes_group = QGroupBox("Дополнительные заметки")
        notes_layout = QVBoxLayout()
        self.notes_edit = QTextEdit()
        self.notes_edit.setMaximumHeight(150)
        notes_layout.addWidget(self.notes_edit)
        notes_group.setLayout(notes_layout)
        layout.addWidget(notes_group)

        # Кнопка сохранения
        save_btn = QPushButton("Сохранить изменения")
        save_btn.setMinimumHeight(40)
        save_btn.clicked.connect(self.save_data)
        layout.addWidget(save_btn)

        layout.addStretch()
        self.setLayout(layout)

    def load_data(self):
        """Загрузка личных данных пользователя"""
        try:
            with open("users.json", 'r', encoding='utf-8') as f:
                users = json.load(f)

            if self.username in users and 'personal_data' in users[self.username]:
                personal_data = users[self.username].get('personal_data', {})

                # Заполняем поля
                self.fields["ФИО:"].setText(personal_data.get('name', ''))

                birth_date = personal_data.get('birth_date', '')
                if birth_date:
                    try:
                        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
                        self.fields["Дата рождения:"].setDate(QDate(date_obj.year, date_obj.month, date_obj.day))
                    except:
                        pass

                self.fields["Адрес:"].setText(personal_data.get('address', ''))
                self.fields["Город:"].setText(personal_data.get('city', ''))
                self.fields["Email:"].setText(personal_data.get('email', ''))
                self.fields["Телефон:"].setText(personal_data.get('phone', ''))
                self.fields["Место работы:"].setText(personal_data.get('workplace', ''))
                self.fields["Должность:"].setText(personal_data.get('position', ''))
                self.notes_edit.setText(personal_data.get('notes', ''))

        except Exception as e:
            print(f"Ошибка загрузки данных: {e}")

    def save_data(self):
        """Сохранение личных данных"""
        try:
            with open("users.json", 'r', encoding='utf-8') as f:
                users = json.load(f)

            if self.username not in users:
                users[self.username] = {}

            if 'personal_data' not in users[self.username]:
                users[self.username]['personal_data'] = {}

            # Сохраняем данные
            personal_data = users[self.username]['personal_data']
            personal_data['name'] = self.fields["ФИО:"].text().strip()
            personal_data['birth_date'] = self.fields["Дата рождения:"].date().toString("yyyy-MM-dd")
            personal_data['address'] = self.fields["Адрес:"].text().strip()
            personal_data['city'] = self.fields["Город:"].text().strip()
            personal_data['email'] = self.fields["Email:"].text().strip()
            personal_data['phone'] = self.fields["Телефон:"].text().strip()
            personal_data['workplace'] = self.fields["Место работы:"].text().strip()
            personal_data['position'] = self.fields["Должность:"].text().strip()
            personal_data['notes'] = self.notes_edit.toPlainText().strip()

            # Сохраняем обратно
            with open("users.json", 'w', encoding='utf-8') as f:
                json.dump(users, f, ensure_ascii=False, indent=2)

            QMessageBox.information(self, "Успех", "Данные успешно сохранены!")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить данные: {str(e)}")


class CategoriesTab(QWidget):
    """Вкладка для управления категориями доходов и расходов"""

    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setup_ui()
        self.load_categories()

    def setup_ui(self):
        main_layout = QHBoxLayout()

        # Категории доходов
        income_group = QGroupBox("Категории доходов")
        income_layout = QVBoxLayout()

        self.income_list = QListWidget()
        self.income_list.setMinimumWidth(200)
        income_layout.addWidget(self.income_list)

        income_btn_layout = QHBoxLayout()
        add_income_btn = QPushButton("Добавить")
        add_income_btn.clicked.connect(lambda: self.add_category('income'))
        edit_income_btn = QPushButton("Изменить")
        edit_income_btn.clicked.connect(lambda: self.edit_category('income'))
        delete_income_btn = QPushButton("Удалить")
        delete_income_btn.clicked.connect(lambda: self.delete_category('income'))

        income_btn_layout.addWidget(add_income_btn)
        income_btn_layout.addWidget(edit_income_btn)
        income_btn_layout.addWidget(delete_income_btn)
        income_layout.addLayout(income_btn_layout)

        income_group.setLayout(income_layout)
        main_layout.addWidget(income_group)

        # Категории расходов
        expense_group = QGroupBox("Категории расходов")
        expense_layout = QVBoxLayout()

        self.expense_list = QListWidget()
        self.expense_list.setMinimumWidth(200)
        expense_layout.addWidget(self.expense_list)

        expense_btn_layout = QHBoxLayout()
        add_expense_btn = QPushButton("Добавить")
        add_expense_btn.clicked.connect(lambda: self.add_category('expense'))
        edit_expense_btn = QPushButton("Изменить")
        edit_expense_btn.clicked.connect(lambda: self.edit_category('expense'))
        delete_expense_btn = QPushButton("Удалить")
        delete_expense_btn.clicked.connect(lambda: self.delete_category('expense'))

        expense_btn_layout.addWidget(add_expense_btn)
        expense_btn_layout.addWidget(edit_expense_btn)
        expense_btn_layout.addWidget(delete_expense_btn)
        expense_layout.addLayout(expense_btn_layout)

        expense_group.setLayout(expense_layout)
        main_layout.addWidget(expense_group)

        self.setLayout(main_layout)

    def load_categories(self):
        """Загрузка категорий из файла пользователя"""
        try:
            with open("users.json", 'r', encoding='utf-8') as f:
                users = json.load(f)

            if self.username in users and 'categories' in users[self.username]:
                categories = users[self.username]['categories']

                # Загружаем категории доходов
                self.income_list.clear()
                for category in categories.get('income', []):
                    self.income_list.addItem(category)

                # Загружаем категории расходов
                self.expense_list.clear()
                for category in categories.get('expense', []):
                    self.expense_list.addItem(category)

        except Exception as e:
            print(f"Ошибка загрузки категорий: {e}")

    def save_categories(self, income_categories, expense_categories):
        """Сохранение категорий в файл пользователя"""
        try:
            with open("users.json", 'r', encoding='utf-8') as f:
                users = json.load(f)

            if self.username not in users:
                users[self.username] = {}

            if 'categories' not in users[self.username]:
                users[self.username]['categories'] = {'income': [], 'expense': []}

            users[self.username]['categories']['income'] = income_categories
            users[self.username]['categories']['expense'] = expense_categories

            with open("users.json", 'w', encoding='utf-8') as f:
                json.dump(users, f, ensure_ascii=False, indent=2)

            return True
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить категории: {str(e)}")
            return False

    def add_category(self, category_type):
        """Добавление новой категории"""
        text, ok = QInputDialog.getText(self, "Добавить категорию",
                                        "Введите название категории:")
        if ok and text.strip():
            if category_type == 'income':
                items = [self.income_list.item(i).text() for i in range(self.income_list.count())]
                if text in items:
                    QMessageBox.warning(self, "Предупреждение", "Такая категория уже существует!")
                    return
                self.income_list.addItem(text.strip())
            else:
                items = [self.expense_list.item(i).text() for i in range(self.expense_list.count())]
                if text in items:
                    QMessageBox.warning(self, "Предупреждение", "Такая категория уже существует!")
                    return
                self.expense_list.addItem(text.strip())

            self.save_current_categories()

    def edit_category(self, category_type):
        """Редактирование категории"""
        if category_type == 'income':
            list_widget = self.income_list
            title = "Изменить категорию дохода"
        else:
            list_widget = self.expense_list
            title = "Изменить категорию расхода"

        current_item = list_widget.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Предупреждение", "Выберите категорию для редактирования!")
            return

        old_text = current_item.text()
        text, ok = QInputDialog.getText(self, title, "Введите новое название:",
                                        text=old_text)
        if ok and text.strip() and text != old_text:
            current_item.setText(text.strip())
            self.save_current_categories()

    def delete_category(self, category_type):
        """Удаление категории"""
        if category_type == 'income':
            list_widget = self.income_list
            title = "Удалить категорию дохода"
        else:
            list_widget = self.expense_list
            title = "Удалить категорию расхода"

        current_item = list_widget.currentItem()
        if not current_item:
            QMessageBox.warning(self, "Предупреждение", "Выберите категорию для удаления!")
            return

        reply = QMessageBox.question(self, title,
                                     f"Вы уверены, что хотите удалить категорию '{current_item.text()}'?",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            row = list_widget.row(current_item)
            list_widget.takeItem(row)
            self.save_current_categories()

    def save_current_categories(self):
        """Сохранение текущих категорий"""
        income_categories = [self.income_list.item(i).text() for i in range(self.income_list.count())]
        expense_categories = [self.expense_list.item(i).text() for i in range(self.expense_list.count())]
        self.save_categories(income_categories, expense_categories)


class TransactionsTab(QWidget):
    """Вкладка для управления транзакциями"""

    def __init__(self, username):
        super().__init__()
        self.username = username
        self.data_file = f"data_{username}.json"
        self.setup_ui()
        self.load_transactions()

    def setup_ui(self):
        main_layout = QVBoxLayout()

        # Форма для добавления транзакции
        form_group = QGroupBox("Добавить транзакцию")
        form_layout = QGridLayout()

        # Тип транзакции
        form_layout.addWidget(QLabel("Тип:"), 0, 0)
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Доход", "Расход"])
        self.type_combo.currentTextChanged.connect(self.on_type_changed)
        form_layout.addWidget(self.type_combo, 0, 1)

        # Категория
        form_layout.addWidget(QLabel("Категория:"), 1, 0)
        self.category_combo = QComboBox()
        form_layout.addWidget(self.category_combo, 1, 1)

        # Сумма
        form_layout.addWidget(QLabel("Сумма:"), 2, 0)
        self.amount_spin = QDoubleSpinBox()
        self.amount_spin.setRange(0, 1000000)
        self.amount_spin.setDecimals(2)
        self.amount_spin.setPrefix("₽ ")
        form_layout.addWidget(self.amount_spin, 2, 1)

        # Дата
        form_layout.addWidget(QLabel("Дата:"), 3, 0)
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("dd.MM.yyyy")
        form_layout.addWidget(self.date_edit, 3, 1)

        # Описание
        form_layout.addWidget(QLabel("Описание:"), 4, 0)
        self.description_edit = QLineEdit()
        self.description_edit.setPlaceholderText("Краткое описание транзакции")
        form_layout.addWidget(self.description_edit, 4, 1)

        # Кнопка добавления
        add_btn = QPushButton("Добавить транзакцию")
        add_btn.clicked.connect(self.add_transaction)
        form_layout.addWidget(add_btn, 5, 0, 1, 2)

        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)

        # Таблица транзакций
        self.transactions_table = QTableWidget()
        self.transactions_table.setColumnCount(6)
        self.transactions_table.setHorizontalHeaderLabels([
            "Дата", "Тип", "Категория", "Сумма", "Описание", "Действия"
        ])
        self.transactions_table.horizontalHeader().setStretchLastSection(True)
        main_layout.addWidget(self.transactions_table)

        # Статистика
        stats_layout = QHBoxLayout()
        self.total_income_label = QLabel("Общий доход: 0 ₽")
        self.total_expense_label = QLabel("Общие расходы: 0 ₽")
        self.balance_label = QLabel("Баланс: 0 ₽")

        stats_layout.addWidget(self.total_income_label)
        stats_layout.addWidget(self.total_expense_label)
        stats_layout.addWidget(self.balance_label)
        stats_layout.addStretch()

        main_layout.addLayout(stats_layout)

        self.setLayout(main_layout)
        self.update_categories()

    def on_type_changed(self):
        """Обновление категорий при изменении типа"""
        self.update_categories()

    def update_categories(self):
        """Обновление списка категорий"""
        try:
            with open("users.json", 'r', encoding='utf-8') as f:
                users = json.load(f)

            if self.username in users and 'categories' in users[self.username]:
                categories = users[self.username]['categories']

                self.category_combo.clear()
                if self.type_combo.currentText() == "Доход":
                    self.category_combo.addItems(categories.get('income', []))
                else:
                    self.category_combo.addItems(categories.get('expense', []))

        except Exception as e:
            print(f"Ошибка загрузки категорий: {e}")

    def load_transactions(self):
        """Загрузка транзакций из файла"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                transactions = data.get('transactions', [])
                self.display_transactions(transactions)
                self.calculate_statistics(transactions)

        except Exception as e:
            print(f"Ошибка загрузки транзакций: {e}")

    def display_transactions(self, transactions):
        """Отображение транзакций в таблице"""
        self.transactions_table.setRowCount(len(transactions))

        for row, transaction in enumerate(reversed(transactions)):  # Новые сверху
            # Дата
            date_item = QTableWidgetItem(transaction.get('date', ''))

            # Тип
            type_item = QTableWidgetItem(transaction.get('type', ''))

            # Категория
            category_item = QTableWidgetItem(transaction.get('category', ''))

            # Сумма
            amount = transaction.get('amount', 0)
            amount_item = QTableWidgetItem(f"{amount:.2f} ₽")

            # Раскрашиваем сумму
            if transaction.get('type') == 'Доход':
                amount_item.setForeground(QColor(0, 128, 0))  # Зеленый
            else:
                amount_item.setForeground(QColor(255, 0, 0))  # Красный

            # Описание
            description_item = QTableWidgetItem(transaction.get('description', ''))

            # Кнопка удаления
            delete_btn = QPushButton("Удалить")
            delete_btn.clicked.connect(lambda checked, r=row: self.delete_transaction(r))

            self.transactions_table.setItem(row, 0, date_item)
            self.transactions_table.setItem(row, 1, type_item)
            self.transactions_table.setItem(row, 2, category_item)
            self.transactions_table.setItem(row, 3, amount_item)
            self.transactions_table.setItem(row, 4, description_item)
            self.transactions_table.setCellWidget(row, 5, delete_btn)

        self.transactions_table.resizeColumnsToContents()

    def add_transaction(self):
        """Добавление новой транзакции"""
        transaction_type = self.type_combo.currentText()
        category = self.category_combo.currentText()
        amount = self.amount_spin.value()
        date = self.date_edit.date().toString("yyyy-MM-dd")
        description = self.description_edit.text().strip()

        if not category:
            QMessageBox.warning(self, "Предупреждение", "Выберите категорию!")
            return

        if amount <= 0:
            QMessageBox.warning(self, "Предупреждение", "Введите сумму больше 0!")
            return

        # Загружаем существующие транзакции
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = {'transactions': []}
        except:
            data = {'transactions': []}

        # Добавляем новую транзакцию
        new_transaction = {
            'id': len(data['transactions']) + 1,
            'type': transaction_type,
            'category': category,
            'amount': amount,
            'date': date,
            'description': description,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data['transactions'].append(new_transaction)

        # Сохраняем
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            # Обновляем отображение
            self.load_transactions()

            # Очищаем форму
            self.description_edit.clear()
            self.amount_spin.setValue(0)

            QMessageBox.information(self, "Успех", "Транзакция добавлена!")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить транзакцию: {str(e)}")

    def delete_transaction(self, row_index):
        """Удаление транзакции"""
        reply = QMessageBox.question(self, "Удаление",
                                     "Вы уверены, что хотите удалить эту транзакцию?",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            try:
                # Загружаем данные
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Удаляем транзакцию (учитываем, что таблица в обратном порядке)
                transactions = data['transactions']
                actual_index = len(transactions) - 1 - row_index

                if 0 <= actual_index < len(transactions):
                    del transactions[actual_index]

                    # Переиндексируем
                    for i, transaction in enumerate(transactions):
                        transaction['id'] = i + 1

                    # Сохраняем
                    with open(self.data_file, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)

                    # Обновляем отображение
                    self.load_transactions()

            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось удалить транзакцию: {str(e)}")

    def calculate_statistics(self, transactions):
        """Расчет статистики"""
        total_income = 0
        total_expense = 0

        for transaction in transactions:
            if transaction['type'] == 'Доход':
                total_income += transaction['amount']
            else:
                total_expense += transaction['amount']

        balance = total_income - total_expense

        self.total_income_label.setText(f"Общий доход: {total_income:.2f} ₽")
        self.total_expense_label.setText(f"Общие расходы: {total_expense:.2f} ₽")
        self.balance_label.setText(f"Баланс: {balance:.2f} ₽")

        # Раскрашиваем баланс
        if balance >= 0:
            self.balance_label.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.balance_label.setStyleSheet("color: red; font-weight: bold;")


class MainWindow(QMainWindow):
    """Главное окно приложения"""

    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle(f"Управление финансами - {username}")
        self.setGeometry(100, 50, 1000, 700)

        self.setup_ui()
        self.load_user_data()

    def setup_ui(self):
        # Центральный виджет с вкладками
        self.tab_widget = QTabWidget()

        # Личные данные
        self.personal_tab = PersonalDataTab({}, self.username)
        self.tab_widget.addTab(self.personal_tab, "Личные данные")

        # Категории
        self.categories_tab = CategoriesTab(self.username)
        self.tab_widget.addTab(self.categories_tab, "Категории")

        # Транзакции
        self.transactions_tab = TransactionsTab(self.username)
        self.tab_widget.addTab(self.transactions_tab, "Транзакции")

        # Сводка (можно добавить позже)
        summary_tab = QWidget()
        summary_layout = QVBoxLayout()
        summary_label = QLabel("Сводка и аналитика\n\n(Здесь будет отображаться статистика и графики)")
        summary_label.setAlignment(Qt.AlignCenter)
        summary_layout.addWidget(summary_label)
        summary_tab.setLayout(summary_layout)
        self.tab_widget.addTab(summary_tab, "Сводка")

        self.setCentralWidget(self.tab_widget)

        # Создаем меню
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()

        # Меню Файл
        file_menu = menubar.addMenu("Файл")
        file_menu.addAction("Экспорт данных", self.export_data)
        file_menu.addAction("Импорт данных", self.import_data)
        file_menu.addSeparator()
        file_menu.addAction("Выход", self.close)

        # Меню Вид
        view_menu = menubar.addMenu("Вид")
        view_menu.addAction("Обновить", self.refresh_data)

        # Меню Справка
        help_menu = menubar.addMenu("Справка")
        help_menu.addAction("О программе", self.show_about)
        help_menu.addAction("Помощь", self.show_help)

    def load_user_data(self):
        """Загрузка данных пользователя"""
        # Данные уже загружаются в соответствующих вкладках
        pass

    def refresh_data(self):
        """Обновление данных во всех вкладках"""
        self.personal_tab.load_data()
        self.categories_tab.load_categories()
        self.transactions_tab.load_transactions()

    def export_data(self):
        """Экспорт данных"""
        try:
            filename = f"finance_export_{self.username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

            # Собираем все данные
            export_data = {}

            # Данные пользователя
            with open("users.json", 'r', encoding='utf-8') as f:
                users = json.load(f)
            export_data['user_info'] = users.get(self.username, {})

            # Транзакции
            data_file = f"data_{self.username}.json"
            if os.path.exists(data_file):
                with open(data_file, 'r', encoding='utf-8') as f:
                    export_data['transactions'] = json.load(f)

            # Сохраняем
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)

            QMessageBox.information(self, "Экспорт", f"Данные успешно экспортированы в файл:\n{filename}")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось экспортировать данные: {str(e)}")

    def import_data(self):
        """Импорт данных"""
        QMessageBox.information(self, "Импорт", "Функция импорта данных будет реализована в следующей версии.")

    def show_about(self):
        """Показать информацию о программе"""
        QMessageBox.about(self, "О программе",
                          "Управление личными финансами\n\n"
                          "Версия 1.0\n"
                          "© 2024 Все права защищены\n\n"
                          "Программа для учета доходов и расходов.")

    def show_help(self):
        """Показать справку"""
        QMessageBox.information(self, "Помощь",
                                "Использование программы:\n\n"
                                "1. Личные данные - заполните информацию о себе\n"
                                "2. Категории - настройте категории доходов и расходов\n"
                                "3. Транзакции - добавляйте и редактируйте операции\n"
                                "4. Сводка - просматривайте статистику\n\n"
                                "Все данные сохраняются автоматически.")


def main():
    app = QApplication(sys.argv)

    # Окно авторизации
    login_window = LoginWindow()

    if login_window.exec_() == QDialog.Accepted:
        # Если авторизация успешна, открываем главное окно
        main_window = MainWindow(login_window.current_user)
        main_window.show()
        sys.exit(app.exec_())
    else:
        sys.exit()


if __name__ == "__main__":
    main()