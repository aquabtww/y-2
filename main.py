import random

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import sys


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.create_button.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.yellow, 3, Qt.SolidLine)
        painter.setPen(pen)

        diameter = random.randint(50, 350)
        painter.drawEllipse(10, 60, diameter, diameter)


# Запуск Виджета
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
    sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
