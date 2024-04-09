from math import sin, cos, pi

from yaml import safe_load
from src.game_objects.game_object import GameObject

from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Bullet(GameObject):

    def __init__(self, location: QPoint, degree: int):
        super().__init__(location, QSize(4, 4), 12, degree)

        with open('config.yml', 'r') as f:
            self._config = safe_load(f)

    def update(self):
        self.x += self._speed * sin(pi / 180 * self._degree)
        self.y -= self._speed * cos(pi / 180 * self._degree)

    def draw(self, painter: QPainter):
        painter.setPen(QPen(QColor(Qt.white), 3))
        painter.translate(self.x, self.y)
        painter.drawRoundedRect(0, 0, self.width, self.height, 1, 1)
        painter.translate(-self.x, -self.y)

    def is_out_of_view(self):
        return not (0 < self.x < self._config['window_width'] and 0 < self.y < self._config['window_height'])
