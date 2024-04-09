from yaml import safe_load

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow

from game import Game


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        with open('config.yml', 'r') as f:
            self._config = safe_load(f)

        self.resize(self._config['window_width'], self._config['window_height'])
        self.setWindowTitle("Asteroids")

        self._game = Game()

        self._timer = QTimer(self)
        self._timer.timeout.connect(self.game_loop)
        self.play()

    def game_loop(self):
        self._game.update()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        self._game.draw(painter)

    def keyPressEvent(self, event):
        keyboard = {
            Qt.Key_W: self._game.start_boosting,
            Qt.Key_D: self._game.start_rotation_to_right,
            Qt.Key_A: self._game.start_rotation_to_left,
            Qt.Key_Space: self._game.shoot
        }
        if event.key() in keyboard:
            keyboard[event.key()]()

    def keyReleaseEvent(self, event):
        keyboard = {
            Qt.Key_W: self._game.stop_boosting,
            Qt.Key_D: self._game.stop_rotation,
            Qt.Key_A: self._game.stop_rotation
        }
        if event.key() in keyboard:
            keyboard[event.key()]()

    def play(self):
        self._timer.start(1000 // self._config['frame_rate'])

    def pause(self):
        self._timer.stop()
