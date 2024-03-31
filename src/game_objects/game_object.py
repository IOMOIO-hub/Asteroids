from src import config

import math

from PyQt5.QtGui import *
from PyQt5.QtCore import *


class GameObject:
    def __init__(self, location: QPoint, size: QSize):
        self.location = location
        self.size = size

        self.speed = 0
        self.degree = 0

    def update(self):
        self.location.setX(int(self.location.x() + self.speed * math.sin(math.pi / 180 * self.degree)))
        self.location.setY(int(self.location.y() - self.speed * math.cos(math.pi / 180 * self.degree)))

        self.location.setX((self.location.x() + config.WINDOW_WIDTH) % config.WINDOW_WIDTH)
        self.location.setY((self.location.y() + config.WINDOW_HEIGHT) % config.WINDOW_HEIGHT)

    def draw(self, painter: QPainter):
        painter.setPen(QColor(Qt.white))
        painter.translate(self.location.x(), self.location.y())
        painter.drawRect(0, 0, self.size.width(), self.size.height())
        painter.translate(-self.location.x(), -self.location.y())

    def isCollide(self, other) -> bool:
        return (self.location.x() < other.location.x() + other.size.width() and
                self.location.x() + self.size.width() > other.location.x() and
                self.location.y() < other.location.y() + other.size.height() and
                self.location.y() + self.size.height() > other.location.y())
