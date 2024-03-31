from src import config

import math
from random import random

from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.game_objects.game_object import GameObject


class Spaceship(GameObject):

    def __init__(self, location: QPoint, size: QSize):
        super().__init__(location, size)

        self.speed_vectors = {}
        self.deceleration = 0.15
        self.boosting = False
        self.shooting = False
        self.rotation_to_right = False
        self.rotation_to_left = False

    def boostSpeed(self):
        self.speed_vectors[self.degree] = min(self.speed_vectors.get(self.degree, 0) + 0.5, 15)

    def update(self):

        if self.boosting: self.boostSpeed()
        if self.rotation_to_right: self.degree += 7.5
        if self.rotation_to_left: self.degree -= 7.5

        keys_to_remove = []
        for degree in self.speed_vectors:
            speed = self.speed_vectors[degree]
            self.location.setX(self.location.x() + speed * math.sin(math.pi / 180 * degree))
            self.location.setY(self.location.y() - speed * math.cos(math.pi / 180 * degree))

            self.speed_vectors[degree] -= self.deceleration
            if self.speed_vectors[degree] <= 0:
                keys_to_remove.append(degree)

        for key in keys_to_remove:
            del self.speed_vectors[key]

        self.location.setX((self.location.x() + config.WINDOW_WIDTH) % config.WINDOW_WIDTH)
        self.location.setY((self.location.y() + config.WINDOW_HEIGHT) % config.WINDOW_HEIGHT)

    def draw(self, painter: QPainter):

        transform = QTransform()
        transform.translate(self.location.x(), self.location.y())
        transform.translate(self.size.width() * 0.5, self.size.height() * 0.5)
        transform.rotate(self.degree)
        transform.translate(-self.size.width() * 0.5, -self.size.height() * 0.5)
        painter.setTransform(transform)

        painter.setPen(QPen(QColor(Qt.white), 3))

        painter.drawLine(self.size.width() // 2, 0, 0, self.size.height())
        painter.drawLine(self.size.width() // 2, 0, self.size.width(), self.size.height())
        painter.drawLine(self.size.width() // 10, self.size.height() // 5 * 4, self.size.width() // 10 * 9,
                         self.size.height() // 5 * 4)

        if self.boosting and random() < 0.75:
            painter.drawLine(self.size.width() // 2, self.size.height(), self.size.width() // 5 * 2,
                             self.size.height() // 5 * 4)
            painter.drawLine(self.size.width() // 2, self.size.height(), self.size.width() // 5 * 3,
                             self.size.height() // 5 * 4)

        painter.setTransform(QTransform())
