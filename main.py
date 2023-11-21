from random import randrange as rand
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.drawBtn.clicked.connect(self.draw)
        self.allow_paint = False

    def draw(self):
        self.allow_paint = True
        self.repaint()
        self.allow_paint = False

    def paintEvent(self, event):
        if not self.allow_paint:
            return
        rad = rand(1, 100)
        pos = (rand(0, self.width() - rad), rand(0, self.height() - rad))
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(rand(0, 256), rand(0, 256), rand(0, 256)))
        painter.drawEllipse(pos[0], pos[1], rad, rad)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = YellowCircles()
    win.show()
    sys.exit(app.exec_())
