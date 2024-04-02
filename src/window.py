import config

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from game import Game


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
        self.setWindowTitle("Asteroids")

        self.game = Game()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.gameLoop)
        self.timer.start(1000 // config.FRAME_RATE)

    def gameLoop(self):
        self.game.update()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.game.draw(painter)

        if config.DEBUG:
            painter.setPen(QColor(Qt.white))
            painter.setFont(QFont('Arial', 8))
            painter.drawText(10, 20, str(self.game.bullets))

    def keyPressEvent(self, event):
        keyboard = {
            Qt.Key_Up: self.game.startBoosting,
            Qt.Key_Right: self.game.startRotationToRight,
            Qt.Key_Left: self.game.startRotationToLeft,
            Qt.Key_Space: self.game.shoot
        }
        if event.key() in keyboard:
            keyboard[event.key()]()

    def keyReleaseEvent(self, event):
        keyboard = {
            Qt.Key_Up: self.game.stopBoosting,
            Qt.Key_Right: self.game.stopRotation,
            Qt.Key_Left: self.game.stopRotation
        }
        if event.key() in keyboard:
            keyboard[event.key()]()
