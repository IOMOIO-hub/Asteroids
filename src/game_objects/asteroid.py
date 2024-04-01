from src import config

import math
from random import uniform

from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.game_objects.game_object import GameObject


class Asteroid(GameObject):
    def __init__(self, location: QPoint, size: QSize):
        super().__init__(location, size)
        self.speed = uniform(0.15, 1)
        self.degree = uniform(0, 359)

    def update(self):
        self.location.setX(int(self.location.x() + self.speed * math.sin(math.pi / 180 * self.degree)))
        self.location.setY(int(self.location.y() - self.speed * math.cos(math.pi / 180 * self.degree)))

        self.location.setX((self.location.x() + config.WINDOW_WIDTH) % config.WINDOW_WIDTH)
        self.location.setY((self.location.y() + config.WINDOW_HEIGHT) % config.WINDOW_HEIGHT)

    def draw(self, painter: QPainter):
        painter.setPen(QColor(Qt.white))
        painter.translate(self.location.x(), self.location.y())
        painter.drawEllipse(self, 0, 0, self.size.width(), self.size.height())
        painter.translate(-self.location.x(), -self.location.y())

