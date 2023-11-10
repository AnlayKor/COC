import sys

from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class RandomFlag(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 400)
        self.base = [20, 80, 100, 30]
        self.button = QPushButton(self)
        self.do_paint = False
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        b = QColor(randrange(256), randrange(256), randrange(256))
        qp.setBrush(b)
        d = randrange(200)
        qp.drawEllipse(randrange(200), randrange(300), d, d)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomFlag()
    ex.show()
    sys.exit(app.exec_())