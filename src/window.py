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
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(1000 // config.FRAME_RATE)

    def game_loop(self):
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
            Qt.Key_W: self.game.start_boosting,
            Qt.Key_D: self.game.start_rotation_to_right,
            Qt.Key_A: self.game.start_rotation_to_left,
            Qt.Key_Space: self.game.shoot
        }
        if event.key() in keyboard:
            keyboard[event.key()]()

    def keyReleaseEvent(self, event):
        keyboard = {
            Qt.Key_W: self.game.stop_boosting,
            Qt.Key_D: self.game.stop_rotation,
            Qt.Key_A: self.game.stop_rotation
        }
        if event.key() in keyboard:
            keyboard[event.key()]()
