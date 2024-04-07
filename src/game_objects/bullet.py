import math

from yaml import safe_load
from src.game_objects.game_object import GameObject

from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Bullet(GameObject):

    def __init__(self, location: QPoint, degree: int):
        super().__init__(location, QSize(4, 4), 12, degree)

        with open('config.yml', 'r') as f:
            self.config = safe_load(f)

    def update(self):
        self.location.setX(int(self.location.x() + self.speed * math.sin(math.pi / 180 * self.degree)))
        self.location.setY(int(self.location.y() - self.speed * math.cos(math.pi / 180 * self.degree)))

    def draw(self, painter: QPainter):
        painter.setPen(QPen(QColor(Qt.white), 2))
        painter.translate(self.location.x(), self.location.y())
        painter.drawRoundedRect(0, 0, self.size.width(), self.size.height(), 1, 1)
        painter.translate(-self.location.x(), -self.location.y())

    def is_out_of_view(self):
        return not (0 <= self.location.x() <= self.config['window_width'] and
                    0 <= self.location.y() <= self.config['window_height'])

    def __repr__(self):
        return f"({self.location.x()}, {self.location.y()})"
