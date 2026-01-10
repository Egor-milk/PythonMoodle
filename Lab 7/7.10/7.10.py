import sys
import webbrowser
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton, QTextBrowser,
                             QTabWidget, QFrame, QDialog, QScrollArea)
from PyQt5.QtCore import Qt, QUrl, QDate
from PyQt5.QtGui import QFont, QIcon, QPixmap, QDesktopServices, QPalette, QColor


class AboutDialog(QDialog):
    """Диалоговое окно 'О программе'"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("О программе")
        self.setFixedSize(600, 550)

        # Настраиваем стиль окна
        self.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
            }
            QLabel {
                color: #333333;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QTabWidget::pane {
                border: 1px solid #dee2e6;
                background-color: white;
                border-radius: 4px;
            }
            QTabBar::tab {
                background-color: #e9ecef;
                padding: 8px 16px;
                margin-right: 2px;
                border-radius: 4px 4px 0 0;
            }
            QTabBar::tab:selected {
                background-color: white;
                border-bottom: 2px solid #007bff;
            }
        """)

        self.setup_ui()

    def setup_ui(self):
        """Настройка пользовательского интерфейса"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Заголовок
        title_label = QLabel("MyApp Pro")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setStyleSheet("color: #007bff;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Версия и дата
        version_label = QLabel("Версия 2.1.0 (Build 2024.05)")
        version_label.setFont(QFont("Arial", 10))
        version_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(version_label)

        # Разделитель
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("background-color: #dee2e6;")
        main_layout.addWidget(separator)

        # Виджет с вкладками
        self.tab_widget = QTabWidget()
        self.tab_widget.setFont(QFont("Arial", 9))

        # Вкладка "Информация"
        self.create_info_tab()

        # Вкладка "Лицензия"
        self.create_license_tab()

        # Вкладка "Контакты"
        self.create_contacts_tab()

        # Вкладка "История версий"
        self.create_changelog_tab()

        main_layout.addWidget(self.tab_widget)

        # Кнопки
        buttons_layout = QHBoxLayout()

        # Кнопка закрытия
        close_button = QPushButton("Закрыть")
        close_button.clicked.connect(self.close)
        close_button.setFixedWidth(100)

        # Кнопка веб-сайта
        website_button = QPushButton("Посетить сайт")
        website_button.clicked.connect(lambda: self.open_url("https://www.example.com"))
        website_button.setFixedWidth(120)

        # Кнопка проверки обновлений
        update_button = QPushButton("Проверить обновления")
        update_button.clicked.connect(self.check_for_updates)
        update_button.setFixedWidth(150)

        buttons_layout.addStretch()
        buttons_layout.addWidget(website_button)
        buttons_layout.addWidget(update_button)
        buttons_layout.addWidget(close_button)

        main_layout.addLayout(buttons_layout)

        # Копирайт
        copyright_label = QLabel(f"© 2020-{datetime.now().year} MyApp Team. Все права защищены.")
        copyright_label.setFont(QFont("Arial", 8))
        copyright_label.setStyleSheet("color: #6c757d;")
        copyright_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(copyright_label)

    def create_info_tab(self):
        """Создает вкладку с общей информацией"""
        info_widget = QWidget()
        layout = QVBoxLayout(info_widget)
        layout.setSpacing(15)

        # Логотип (заглушка)
        logo_label = QLabel("🖥️")
        logo_label.setFont(QFont("Arial", 48))
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)

        # Описание программы
        description = QLabel(
            "<h3>Профессиональное программное обеспечение для управления данными</h3>"
            "<p>MyApp Pro - это мощное решение для обработки, анализа и визуализации данных. "
            "Программа предназначена для профессионального использования в бизнесе, "
            "научных исследованиях и образовательных целях.</p>"
            "<p>Основные возможности:</p>"
            "<ul>"
            "<li>Импорт данных из различных форматов (CSV, Excel, JSON)</li>"
            "<li>Расширенная аналитика и статистика</li>"
            "<li>Визуализация данных с помощью графиков и диаграмм</li>"
            "<li>Автоматизация рутинных задач</li>"
            "<li>Работа с базами данных</li>"
            "<li>Генерация отчетов</li>"
            "</ul>"
        )
        description.setWordWrap(True)
        description.setOpenExternalLinks(True)
        layout.addWidget(description)

        self.tab_widget.addTab(info_widget, "Информация")

    def create_license_tab(self):
        """Создает вкладку с лицензионным соглашением"""
        license_widget = QWidget()
        layout = QVBoxLayout(license_widget)

        # Прокручиваемая область для лицензии
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        license_text = QTextBrowser()
        license_text.setPlainText(self.get_license_text())
        license_text.setFont(QFont("Arial", 9))
        license_text.setReadOnly(True)

        scroll_area.setWidget(license_text)
        layout.addWidget(scroll_area)

        # Чекбокс принятия лицензии
        self.license_checkbox = QLabel(
            "<p style='color: green; font-weight: bold;'>✓ Лицензионное соглашение принято</p>"
            "<p><small>Лицензия: Commercial Edition</small></p>"
            "<p><small>Ключ продукта: MYP-2024-XXXX-YYYY-ZZZZ</small></p>"
        )
        layout.addWidget(self.license_checkbox)

        self.tab_widget.addTab(license_widget, "Лицензия")

    def create_contacts_tab(self):
        """Создает вкладку с контактной информацией"""
        contacts_widget = QWidget()
        layout = QVBoxLayout(contacts_widget)
        layout.setSpacing(20)

        # Контактная информация
        contacts_info = QLabel(
            "<h3>Контактная информация</h3>"
            "<p><b>Компания:</b> MyApp Technologies Inc.</p>"
            "<p><b>Адрес:</b> 123456, г. Москва, ул. Программистов, д. 1</p>"
            "<p><b>Телефон:</b> +7 (495) 123-45-67</p>"
            "<p><b>Техническая поддержка:</b> +7 (800) 123-45-67 (бесплатно)</p>"
            "<hr>"
            "<h4>Электронная почта:</h4>"
            "<p>📧 <b>Общие вопросы:</b> <a href='mailto:info@myapp.com'>info@myapp.com</a></p>"
            "<p>📧 <b>Техническая поддержка:</b> <a href='mailto:support@myapp.com'>support@myapp.com</a></p>"
            "<p>📧 <b>Отдел продаж:</b> <a href='mailto:sales@myapp.com'>sales@myapp.com</a></p>"
            "<p>📧 <b>Сотрудничество:</b> <a href='mailto:partners@myapp.com'>partners@myapp.com</a></p>"
            "<hr>"
            "<h4>Онлайн ресурсы:</h4>"
            "<p>🌐 <b>Официальный сайт:</b> <a href='https://www.myapp.com'>www.myapp.com</a></p>"
            "<p>💼 <b>LinkedIn:</b> <a href='https://linkedin.com/company/myapp'>linkedin.com/company/myapp</a></p>"
            "<p>📱 <b>Twitter:</b> <a href='https://twitter.com/myapp'>@myapp</a></p>"
            "<p>📹 <b>YouTube:</b> <a href='https://youtube.com/c/myapp'>YouTube канал</a></p>"
        )
        contacts_info.setWordWrap(True)
        contacts_info.setOpenExternalLinks(True)
        contacts_info.linkActivated.connect(self.open_url)

        layout.addWidget(contacts_info)

        # Кнопки быстрой связи
        buttons_layout = QHBoxLayout()

        email_button = QPushButton("Написать письмо")
        email_button.clicked.connect(lambda: self.open_url("mailto:support@myapp.com"))

        call_button = QPushButton("Позвонить")
        call_button.clicked.connect(lambda: self.open_url("tel:+74951234567"))

        website_button = QPushButton("Открыть сайт")
        website_button.clicked.connect(lambda: self.open_url("https://www.myapp.com"))

        buttons_layout.addWidget(email_button)
        buttons_layout.addWidget(call_button)
        buttons_layout.addWidget(website_button)

        layout.addLayout(buttons_layout)

        self.tab_widget.addTab(contacts_widget, "Контакты")

    def create_changelog_tab(self):
        """Создает вкладку с историей версий"""
        changelog_widget = QWidget()
        layout = QVBoxLayout(changelog_widget)

        changelog_text = QTextBrowser()
        changelog_text.setPlainText(self.get_changelog_text())
        changelog_text.setFont(QFont("Arial", 9))
        changelog_text.setReadOnly(True)

        layout.addWidget(changelog_text)

        self.tab_widget.addTab(changelog_widget, "История версий")

    def get_license_text(self):
        """Возвращает текст лицензионного соглашения"""
        return """
ЛИЦЕНЗИОННОЕ СОГЛАШЕНИЕ НА ИСПОЛЬЗОВАНИЕ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ
MyApp Pro (Версия 2.1.0)

1. ПРЕДМЕТ СОГЛАШЕНИЯ
Настоящее Лицензионное соглашение (далее – "Соглашение") регулирует отношения 
между MyApp Technologies Inc. (далее – "Лицензиар") и пользователем (далее – "Лицензиат") 
по использованию программного обеспечения MyApp Pro (далее – "Программа").

2. ПРЕДОСТАВЛЕНИЕ ЛИЦЕНЗИИ
Лицензиар предоставляет Лицензиату неисключительную, непередаваемую лицензию 
на использование Программы на одном компьютере.

3. ОГРАНИЧЕНИЯ
Лицензиат не имеет права:
- Копировать, модифицировать или распространять Программу;
- Разбирать Программу на составляющие коды, декомпилировать или дизассемблировать;
- Передавать лицензию третьим лицам.

4. ГАРАНТИИ
Программа предоставляется "как есть". Лицензиар не предоставляет гарантий 
относительно бесперебойной работы Программы.

5. ОТВЕТСТВЕННОСТЬ
Лицензиар не несет ответственности за любые косвенные убытки, возникшие 
в результате использования или невозможности использования Программы.

6. СРОК ДЕЙСТВИЯ
Настоящее Соглашение действует бессрочно с момента установки Программы.

7. ЗАКЛЮЧИТЕЛЬНЫЕ ПОЛОЖЕНИЯ
Настоящее Соглашение составлено в соответствии с законодательством Российской Федерации.
"""

    def get_changelog_text(self):
        """Возвращает историю изменений"""
        return """
ИСТОРИЯ ВЕРСИЙ MyApp Pro

═══════════════════════════════════════════════════════════════════════════════

ВЕРСИЯ 2.1.0 (Май 2024)
───────────────────────────────────────────────────────────────────────────────
НОВЫЕ ВОЗМОЖНОСТИ:
• Добавлена поддержка импорта данных из Google Sheets
• Реализован экспорт отчетов в формате PDF
• Добавлены новые типы диаграмм (тепловые карты, пузырьковые диаграммы)

УЛУЧШЕНИЯ:
• Ускорена обработка больших данных на 40%
• Улучшен интерфейс пользователя
• Оптимизировано использование памяти

ИСПРАВЛЕНИЯ ОШИБОК:
• Исправлена ошибка сохранения настроек
• Исправлена проблема с кодировкой при импорте CSV
• Исправлены мелкие баги в модуле визуализации

───────────────────────────────────────────────────────────────────────────────

ВЕРСИЯ 2.0.3 (Март 2024)
───────────────────────────────────────────────────────────────────────────────
• Добавлена поддержка русского языка
• Улучшена совместимость с Windows 11
• Исправлены проблемы безопасности

───────────────────────────────────────────────────────────────────────────────

ВЕРСИЯ 2.0.0 (Январь 2024)
───────────────────────────────────────────────────────────────────────────────
• Полный редизайн интерфейса
• Добавлен модуль машинного обучения
• Поддержка облачной синхронизации
• Новая система отчетности

───────────────────────────────────────────────────────────────────────────────

ВЕРСИЯ 1.5.2 (Октябрь 2023)
───────────────────────────────────────────────────────────────────────────────
• Добавлена поддержка формата JSON
• Улучшена производительность
• Исправлены ошибки экспорта в Excel

───────────────────────────────────────────────────────────────────────────────

ВЕРСИЯ 1.0.0 (Июнь 2023)
───────────────────────────────────────────────────────────────────────────────
• Первый выпуск программы
• Базовые функции импорта/экспорта данных
• Основные типы графиков и диаграмм
• Система управления проектами
"""

    def open_url(self, url):
        """Открывает URL в браузере по умолчанию"""
        try:
            QDesktopServices.openUrl(QUrl(url))
        except Exception as e:
            print(f"Не удалось открыть URL: {e}")

    def check_for_updates(self):
        """Проверяет наличие обновлений"""
        from PyQt5.QtWidgets import QMessageBox

        QMessageBox.information(self, "Проверка обновлений",
                                "Вы используете последнюю версию программы.\n"
                                "Версия 2.1.0 актуальна на " + datetime.now().strftime("%d.%m.%Y"))


class MainWindow(QMainWindow):
    """Главное окно приложения с кнопкой 'О программе'"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyApp Pro - Главное окно")
        self.setGeometry(100, 100, 800, 600)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Заголовок
        title_label = QLabel("Добро пожаловать в MyApp Pro!")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Основное содержимое
        content_label = QLabel(
            "<p>Это главное окно приложения. Для просмотра информации о программе "
            "нажмите кнопку 'О программе' в меню или на панели инструментов.</p>"
        )
        content_label.setWordWrap(True)
        content_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(content_label)

        layout.addStretch()

        # Кнопка для открытия окна "О программе"
        about_button = QPushButton("О программе")
        about_button.setFont(QFont("Arial", 12))
        about_button.setFixedSize(150, 40)
        about_button.clicked.connect(self.show_about_dialog)
        layout.addWidget(about_button, alignment=Qt.AlignCenter)

        layout.addStretch()

        # Создаем меню
        self.create_menu()

    def create_menu(self):
        """Создает меню приложения"""
        menubar = self.menuBar()

        # Меню "Справка"
        help_menu = menubar.addMenu("Справка")

        # Пункт "О программе"
        about_action = help_menu.addAction("О программе")
        about_action.triggered.connect(self.show_about_dialog)

        # Пункт "Проверить обновления"
        update_action = help_menu.addAction("Проверить обновления")
        update_action.triggered.connect(self.check_updates)

        help_menu.addSeparator()

        # Пункт "Документация"
        docs_action = help_menu.addAction("Открыть документацию")
        docs_action.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("https://docs.myapp.com")))

        # Пеню "Файл"
        file_menu = menubar.addMenu("Файл")
        file_menu.addAction("Выход", self.close)

    def show_about_dialog(self):
        """Показывает диалоговое окно 'О программе'"""
        dialog = AboutDialog(self)
        dialog.exec_()

    def check_updates(self):
        """Проверяет обновления из главного меню"""
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(self, "Обновления",
                                "Проверка обновлений...\n"
                                "Текущая версия: 2.1.0\n"
                                "Статус: Актуальна")


def main():
    app = QApplication(sys.argv)

    # Устанавливаем иконку приложения
    app.setWindowIcon(QIcon("icon.ico"))

    # Настраиваем стиль приложения
    app.setStyle("Fusion")

    # Создаем и показываем главное окно
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()