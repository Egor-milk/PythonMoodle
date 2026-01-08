import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from enum import Enum


class ShapeType(Enum):
    LINE = 1
    RECTANGLE = 2
    ELLIPSE = 3
    TRIANGLE = 4


class GraphicsEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initDrawing()

    def initUI(self):
        # Основные настройки окна
        self.setWindowTitle('Графический редактор')
        self.setGeometry(100, 100, 1000, 700)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Главный layout
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Левая панель инструментов
        left_panel = QVBoxLayout()

        # Выбор фигур
        shapes_group = QGroupBox("Фигуры")
        shapes_layout = QVBoxLayout()

        self.shape_buttons = {}
        for shape in ShapeType:
            btn = QRadioButton(shape.name.capitalize())
            btn.shape_type = shape
            shapes_layout.addWidget(btn)
            self.shape_buttons[shape] = btn

        self.shape_buttons[ShapeType.LINE].setChecked(True)
        self.current_shape = ShapeType.LINE
        shapes_group.setLayout(shapes_layout)

        # Настройки цвета и толщины
        settings_group = QGroupBox("Настройки")
        settings_layout = QVBoxLayout()

        # Цвет контура
        self.border_color = QColor(0, 0, 0)
        self.border_color_btn = QPushButton('Цвет контура')
        self.border_color_btn.clicked.connect(self.chooseBorderColor)
        settings_layout.addWidget(self.border_color_btn)

        # Цвет заливки
        self.fill_color = QColor(255, 255, 255)
        self.fill_color_btn = QPushButton('Цвет заливки')
        self.fill_color_btn.clicked.connect(self.chooseFillColor)
        settings_layout.addWidget(self.fill_color_btn)

        # Толщина линии
        thickness_layout = QHBoxLayout()
        thickness_layout.addWidget(QLabel('Толщина:'))
        self.thickness_spin = QSpinBox()
        self.thickness_spin.setRange(1, 20)
        self.thickness_spin.setValue(2)
        thickness_layout.addWidget(self.thickness_spin)
        settings_layout.addLayout(thickness_layout)

        # Стиль линии
        self.line_style_combo = QComboBox()
        self.line_style_combo.addItems(['Solid', 'Dash', 'Dot', 'DashDot', 'DashDotDot'])
        settings_layout.addWidget(QLabel('Стиль линии:'))
        settings_layout.addWidget(self.line_style_combo)

        settings_group.setLayout(settings_layout)

        # Кнопки действий
        self.clear_btn = QPushButton('Очистить')
        self.clear_btn.clicked.connect(self.clearCanvas)

        self.undo_btn = QPushButton('Отменить')
        self.undo_btn.clicked.connect(self.undo)

        # Добавление виджетов в левую панель
        left_panel.addWidget(shapes_group)
        left_panel.addWidget(settings_group)
        left_panel.addWidget(self.clear_btn)
        left_panel.addWidget(self.undo_btn)
        left_panel.addStretch()

        # Область рисования
        self.canvas = CanvasWidget()

        # Добавление в главный layout
        main_layout.addLayout(left_panel, 1)
        main_layout.addWidget(self.canvas, 4)

        # Подключение сигналов
        for btn in self.shape_buttons.values():
            btn.toggled.connect(self.shapeChanged)

    def initDrawing(self):
        self.start_point = None
        self.end_point = None

    def shapeChanged(self):
        for shape, btn in self.shape_buttons.items():
            if btn.isChecked():
                self.current_shape = shape
                break

    def chooseBorderColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.border_color = color
            self.canvas.setBorderColor(color)

    def chooseFillColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.fill_color = color
            self.canvas.setFillColor(color)

    def clearCanvas(self):
        self.canvas.clear()

    def undo(self):
        self.canvas.undo()


class CanvasWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.initCanvas()

        # Настройки по умолчанию
        self.border_color = QColor(0, 0, 0)
        self.fill_color = QColor(255, 255, 255)
        self.line_width = 2
        self.line_style = Qt.SolidLine

        self.shapes = []
        self.temp_shape = None
        self.drawing = False

    def initCanvas(self):
        self.setMinimumSize(600, 500)
        self.setStyleSheet("background-color: white; border: 2px solid gray;")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.start_point = event.pos()
            self.end_point = event.pos()

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawing = False
            shape = {
                'type': self.parent().parent().current_shape,
                'start': self.start_point,
                'end': self.end_point,
                'border_color': self.border_color,
                'fill_color': self.fill_color,
                'line_width': self.line_width,
                'line_style': self.line_style
            }
            self.shapes.append(shape)
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Рисуем все сохраненные фигуры
        for shape in self.shapes:
            self.drawShape(painter, shape)

        # Рисуем временную фигуру (при рисовании)
        if self.drawing:
            temp_shape = {
                'type': self.parent().parent().current_shape,
                'start': self.start_point,
                'end': self.end_point,
                'border_color': self.border_color,
                'fill_color': self.fill_color,
                'line_width': self.line_width,
                'line_style': self.line_style
            }
            self.drawShape(painter, temp_shape)

    def drawShape(self, painter, shape):
        pen = QPen(shape['border_color'], shape['line_width'])

        # Установка стиля линии
        style_map = {
            'Solid': Qt.SolidLine,
            'Dash': Qt.DashLine,
            'Dot': Qt.DotLine,
            'DashDot': Qt.DashDotLine,
            'DashDotDot': Qt.DashDotDotLine
        }
        pen.setStyle(style_map.get(self.parent().parent().line_style_combo.currentText(), Qt.SolidLine))
        painter.setPen(pen)

        brush = QBrush(shape['fill_color'])
        painter.setBrush(brush)

        # Вычисление координат
        x1, y1 = shape['start'].x(), shape['start'].y()
        x2, y2 = shape['end'].x(), shape['end'].y()

        # Рисование выбранной фигуры
        if shape['type'] == ShapeType.LINE:
            painter.drawLine(x1, y1, x2, y2)

        elif shape['type'] == ShapeType.RECTANGLE:
            painter.drawRect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))

        elif shape['type'] == ShapeType.ELLIPSE:
            painter.drawEllipse(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))

        elif shape['type'] == ShapeType.TRIANGLE:
            polygon = QPolygon()
            polygon.append(QPoint(x1, y2))
            polygon.append(QPoint((x1 + x2) // 2, y1))
            polygon.append(QPoint(x2, y2))
            painter.drawPolygon(polygon)

    def setBorderColor(self, color):
        self.border_color = color

    def setFillColor(self, color):
        self.fill_color = color

    def clear(self):
        self.shapes = []
        self.update()

    def undo(self):
        if self.shapes:
            self.shapes.pop()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = GraphicsEditor()
    editor.show()
    sys.exit(app.exec_())