from yaml import safe_load

import math

from PyQt5.QtGui import *
from PyQt5.QtCore import *


class GameObject:
    def __init__(self, location: QPoint, size: QSize, speed: float = 0, degree: int = 0):
        self.location = location
        self.size = size

        self.speed = speed
        self.degree = degree

        with open('config.yml', 'r') as f:
            self.config = safe_load(f)

    def update(self):
        self.location.setX(int(self.location.x() + self.speed * math.sin(math.pi / 180 * self.degree)))
        self.location.setY(int(self.location.y() - self.speed * math.cos(math.pi / 180 * self.degree)))

        self.location.setX((self.location.x() + self.config['window_width']) % self.config['window_width'])
        self.location.setY((self.location.y() + self.config['window_height']) % self.config['window_height'])

    def draw(self, painter: QPainter):
        painter.setPen(QColor(Qt.white))
        painter.translate(self.location.x(), self.location.y())
        painter.drawRect(0, 0, self.size.width(), self.size.height())
        painter.translate(-self.location.x(), -self.location.y())

    def is_collide(self, other) -> bool:
        return (self.location.x() < other.location.x() + other.size.width() and
                self.location.x() + self.size.width() > other.location.x() and
                self.location.y() < other.location.y() + other.size.height() and
                self.location.y() + self.size.height() > other.location.y())
