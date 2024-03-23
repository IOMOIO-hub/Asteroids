import sys
from time import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class GameWidget(QWidget):

    def __init__(self, width, height):
        super().__init__()

        self.width = width
        self.height = height
        self.resize(width, height)

        self.initGameLoop()

    def initGameLoop(self):
        self.timer = QTimer(None)
        self.timer.timeout.connect(self.gameLoop)
        self.timer.start(1000 // 60)  # 60 FPS

    def gameLoop(self):
        # ...
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(0, 0, self.width, self.height, QBrush(Qt.SolidPattern))

        painter.setPen(QColor(Qt.white))
        painter.setFont(QFont('Arial', 20))
        painter.drawText(10, 50, str(time()))

        painter.end()


class Window(QMainWindow):
    WIDTH = 1080
    HEIGHT = 720

    def __init__(self):
        super().__init__()
        self.resize(self.WIDTH, self.HEIGHT)
        self.setWindowTitle("Asteroids")

        game = GameWidget(self.WIDTH, self.HEIGHT)
        self.setCentralWidget(game)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
