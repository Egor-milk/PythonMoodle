import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class TextNotepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.initUI()

    def initUI(self):
        # Создание центрального виджета
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Создание главного меню
        self.createMenus()

        # Создание панели инструментов
        self.createToolbar()

        # Создание строки состояния
        self.statusBar().showMessage('Готово')

        # Настройки окна
        self.setWindowTitle('Текстовый блокнот')
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def createMenus(self):
        # Меню "Файл"
        file_menu = self.menuBar().addMenu('Файл')

        # Новый файл
        new_action = QAction(QIcon(), 'Новый', self)
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('Создать новый файл')
        new_action.triggered.connect(self.newFile)
        file_menu.addAction(new_action)

        # Открыть файл
        open_action = QAction(QIcon(), 'Открыть', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Открыть текстовый файл')
        open_action.triggered.connect(self.openFile)
        file_menu.addAction(open_action)

        # Сохранить
        save_action = QAction(QIcon(), 'Сохранить', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Сохранить текущий файл')
        save_action.triggered.connect(self.saveFile)
        file_menu.addAction(save_action)

        # Сохранить как
        save_as_action = QAction(QIcon(), 'Сохранить как...', self)
        save_as_action.setStatusTip('Сохранить файл с новым именем')
        save_as_action.triggered.connect(self.saveFileAs)
        file_menu.addAction(save_as_action)

        file_menu.addSeparator()

        # Выход
        exit_action = QAction(QIcon(), 'Выход', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Выйти из программы')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Меню "Правка"
        edit_menu = self.menuBar().addMenu('Правка')

        # Отменить
        undo_action = QAction(QIcon(), 'Отменить', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.triggered.connect(self.text_edit.undo)
        edit_menu.addAction(undo_action)

        # Повторить
        redo_action = QAction(QIcon(), 'Повторить', self)
        redo_action.setShortcut('Ctrl+Y')
        redo_action.triggered.connect(self.text_edit.redo)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        # Вырезать
        cut_action = QAction(QIcon(), 'Вырезать', self)
        cut_action.setShortcut('Ctrl+X')
        cut_action.triggered.connect(self.text_edit.cut)
        edit_menu.addAction(cut_action)

        # Копировать
        copy_action = QAction(QIcon(), 'Копировать', self)
        copy_action.setShortcut('Ctrl+C')
        copy_action.triggered.connect(self.text_edit.copy)
        edit_menu.addAction(copy_action)

        # Вставить
        paste_action = QAction(QIcon(), 'Вставить', self)
        paste_action.setShortcut('Ctrl+V')
        paste_action.triggered.connect(self.text_edit.paste)
        edit_menu.addAction(paste_action)

        # Выделить все
        select_all_action = QAction(QIcon(), 'Выделить все', self)
        select_all_action.setShortcut('Ctrl+A')
        select_all_action.triggered.connect(self.text_edit.selectAll)
        edit_menu.addAction(select_all_action)

        edit_menu.addSeparator()

        # Найти
        find_action = QAction(QIcon(), 'Найти', self)
        find_action.setShortcut('Ctrl+F')
        find_action.triggered.connect(self.findText)
        edit_menu.addAction(find_action)

        # Меню "Вид"
        view_menu = self.menuBar().addMenu('Вид')

        # Увеличить шрифт
        zoom_in_action = QAction(QIcon(), 'Увеличить шрифт', self)
        zoom_in_action.setShortcut('Ctrl++')
        zoom_in_action.triggered.connect(self.zoomIn)
        view_menu.addAction(zoom_in_action)

        # Уменьшить шрифт
        zoom_out_action = QAction(QIcon(), 'Уменьшить шрифт', self)
        zoom_out_action.setShortcut('Ctrl+-')
        zoom_out_action.triggered.connect(self.zoomOut)
        view_menu.addAction(zoom_out_action)

        # Сбросить масштаб
        zoom_reset_action = QAction(QIcon(), 'Сбросить масштаб', self)
        zoom_reset_action.setShortcut('Ctrl+0')
        zoom_reset_action.triggered.connect(self.zoomReset)
        view_menu.addAction(zoom_reset_action)

        view_menu.addSeparator()

        # Перенос слов
        word_wrap_action = QAction(QIcon(), 'Перенос слов', self)
        word_wrap_action.setCheckable(True)
        word_wrap_action.setChecked(True)
        word_wrap_action.triggered.connect(self.toggleWordWrap)
        view_menu.addAction(word_wrap_action)

        # Меню "Справка"
        help_menu = self.menuBar().addMenu('Справка')

        # О программе
        about_action = QAction(QIcon(), 'О программе', self)
        about_action.triggered.connect(self.showAbout)
        help_menu.addAction(about_action)

    def createToolbar(self):
        # Панель инструментов "Файл"
        file_toolbar = self.addToolBar('Файл')

        # Новый
        new_action = QAction(QIcon.fromTheme('document-new'), 'Новый', self)
        new_action.triggered.connect(self.newFile)
        file_toolbar.addAction(new_action)

        # Открыть
        open_action = QAction(QIcon.fromTheme('document-open'), 'Открыть', self)
        open_action.triggered.connect(self.openFile)
        file_toolbar.addAction(open_action)

        # Сохранить
        save_action = QAction(QIcon.fromTheme('document-save'), 'Сохранить', self)
        save_action.triggered.connect(self.saveFile)
        file_toolbar.addAction(save_action)

        file_toolbar.addSeparator()

        # Панель инструментов "Правка"
        edit_toolbar = QToolBar('Правка')
        self.addToolBar(edit_toolbar)

        # Вырезать
        cut_action = QAction(QIcon.fromTheme('edit-cut'), 'Вырезать', self)
        cut_action.triggered.connect(self.text_edit.cut)
        edit_toolbar.addAction(cut_action)

        # Копировать
        copy_action = QAction(QIcon.fromTheme('edit-copy'), 'Копировать', self)
        copy_action.triggered.connect(self.text_edit.copy)
        edit_toolbar.addAction(copy_action)

        # Вставить
        paste_action = QAction(QIcon.fromTheme('edit-paste'), 'Вставить', self)
        paste_action.triggered.connect(self.text_edit.paste)
        edit_toolbar.addAction(paste_action)

    def newFile(self):
        if self.checkUnsavedChanges():
            self.text_edit.clear()
            self.current_file = None
            self.setWindowTitle('Текстовый блокнот - Новый файл')
            self.statusBar().showMessage('Новый файл создан')

    def openFile(self):
        if self.checkUnsavedChanges():
            file_name, _ = QFileDialog.getOpenFileName(
                self, 'Открыть файл', '', 'Текстовые файлы (*.txt);;Все файлы (*)'
            )

            if file_name:
                try:
                    with open(file_name, 'r', encoding='utf-8') as file:
                        content = file.read()
                        self.text_edit.setText(content)

                    self.current_file = file_name
                    self.setWindowTitle(f'Текстовый блокнот - {os.path.basename(file_name)}')
                    self.statusBar().showMessage(f'Файл открыт: {file_name}')
                except Exception as e:
                    QMessageBox.critical(self, 'Ошибка', f'Не удалось открыть файл:\n{str(e)}')

    def saveFile(self):
        if self.current_file:
            try:
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(self.text_edit.toPlainText())
                self.statusBar().showMessage(f'Файл сохранен: {self.current_file}')
                return True
            except Exception as e:
                QMessageBox.critical(self, 'Ошибка', f'Не удалось сохранить файл:\n{str(e)}')
                return False
        else:
            return self.saveFileAs()

    def saveFileAs(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, 'Сохранить как', '', 'Текстовые файлы (*.txt);;Все файлы (*)'
        )

        if file_name:
            if not file_name.endswith('.txt'):
                file_name += '.txt'

            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(self.text_edit.toPlainText())

                self.current_file = file_name
                self.setWindowTitle(f'Текстовый блокнот - {os.path.basename(file_name)}')
                self.statusBar().showMessage(f'Файл сохранен: {file_name}')
                return True
            except Exception as e:
                QMessageBox.critical(self, 'Ошибка', f'Не удалось сохранить файл:\n{str(e)}')
                return False
        return False

    def checkUnsavedChanges(self):
        if self.text_edit.document().isModified():
            reply = QMessageBox.question(
                self, 'Несохраненные изменения',
                'У вас есть несохраненные изменения. Сохранить?',
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
            )

            if reply == QMessageBox.Save:
                return self.saveFile()
            elif reply == QMessageBox.Cancel:
                return False

        return True

    def findText(self):
        text, ok = QInputDialog.getText(self, 'Найти', 'Введите текст для поиска:')
        if ok and text:
            found = self.text_edit.find(text)
            if not found:
                QMessageBox.information(self, 'Поиск', f'Текст "{text}" не найден.')

    def zoomIn(self):
        font = self.text_edit.font()
        font.setPointSize(font.pointSize() + 1)
        self.text_edit.setFont(font)

    def zoomOut(self):
        font = self.text_edit.font()
        if font.pointSize() > 6:
            font.setPointSize(font.pointSize() - 1)
            self.text_edit.setFont(font)

    def zoomReset(self):
        font = self.text_edit.font()
        font.setPointSize(10)
        self.text_edit.setFont(font)

    def toggleWordWrap(self):
        if self.text_edit.lineWrapMode() == QTextEdit.NoWrap:
            self.text_edit.setLineWrapMode(QTextEdit.WidgetWidth)
        else:
            self.text_edit.setLineWrapMode(QTextEdit.NoWrap)

    def showAbout(self):
        QMessageBox.about(self, 'О программе',
                          '<h2>Текстовый блокнот</h2>'
                          '<p>Версия 1.0</p>'
                          '<p>Простой текстовый редактор с поддержкой:</p>'
                          '<ul>'
                          '<li>Открытия текстовых файлов (.txt)</li>'
                          '<li>Редактирования текста</li>'
                          '<li>Сохранения изменений</li>'
                          '<li>Поиска текста</li>'
                          '<li>Изменения размера шрифта</li>'
                          '</ul>'
                          '<p>Разработано на PyQt5</p>')

    def closeEvent(self, event):
        if self.checkUnsavedChanges():
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Установка стиля
    app.setStyle('Fusion')

    # Создание и запуск приложения
    notepad = TextNotepad()
    sys.exit(app.exec_())