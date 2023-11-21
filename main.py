import random
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.drawBtn.clicked.connect(self.draw)
        self.allow_paint = False

    def draw(self):
        self.allow_paint = True
        self.repaint()
        self.allow_paint = False

    def paintEvent(self, event):
        if not self.allow_paint:
            return
        rad = random.randrange(1, 100)
        pos = (random.randrange(0, self.width() - rad), random.randrange(0, self.height() - rad))
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(255, 255, 0))
        painter.drawEllipse(pos[0], pos[1], rad, rad)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = YellowCircles()
    win.show()
    sys.exit(app.exec_())
