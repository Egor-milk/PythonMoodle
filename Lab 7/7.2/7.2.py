import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt


class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Создаем метку с фразой
        label = QLabel('Каждый охотник желает знать, где сидят фазаны', self)
        label.setAlignment(Qt.AlignCenter)

        # Настройки окна
        self.setGeometry(300, 300, 500, 100)
        self.setWindowTitle('Цвета радуги')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleApp()
    sys.exit(app.exec_())