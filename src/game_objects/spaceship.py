from src import config

import math
from random import random

from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.game_objects.game_object import GameObject


class Spaceship(GameObject):

    def __init__(self):
        super().__init__(
            QPoint((config.WINDOW_WIDTH - 30) // 2, (config.WINDOW_HEIGHT - 40) // 2),
            QSize(45, 60)
        )

        self.speed_vectors = {}
        self.deceleration = 0.125
        self.boosting = False
        self.shooting = False
        self.rotation_to_right = False
        self.rotation_to_left = False

    def boost_speed(self):
        self.speed_vectors[self.degree] = min(self.speed_vectors.get(self.degree, 0) + 0.4, 12.5)

    def reset(self):
        self.location.setX((config.WINDOW_WIDTH - self.size.width()) // 2)
        self.location.setY((config.WINDOW_HEIGHT - self.size.height()) // 2)
        self.speed_vectors = {}
        self.degree = 0

    def update(self):

        if self.boosting: self.boost_speed()
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
        width = self.size.width()
        height = self.size.height()

        transform = QTransform()
        transform.translate(self.location.x(), self.location.y())
        transform.translate(width // 2, height // 2)
        transform.rotate(self.degree)
        transform.translate(-width // 2, -height // 2)
        painter.setTransform(transform)

        painter.setPen(QPen(QColor(Qt.white), 3))

        painter.drawLine(width // 2, 0, 0, height)
        painter.drawLine(width // 2, 0, width, height)
        painter.drawLine(width // 10, height // 5 * 4, width // 10 * 9, height // 5 * 4)

        if self.boosting and random() < 0.75:
            painter.drawLine(width // 2, height + 10, width // 10 * 3, height // 5 * 4)
            painter.drawLine(width // 2, height + 10, width // 10 * 7, height // 5 * 4)

        painter.setTransform(QTransform())
