from yaml import safe_load

from math import sin, cos, pi
from random import random

from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.game_objects.game_object import GameObject


class Spaceship(GameObject):

    def __init__(self):

        with open('config.yml', 'r') as f:
            self._config = safe_load(f)

        super().__init__(
            QPoint((self._config['window_width'] - 60) // 2, (self._config['window_height'] - 45) // 2),
            QSize(45, 60)
        )

        self._speed_vectors = {}
        self._deceleration = 0.125

        self.boosting = False
        self.shooting = False
        self.rotation_factor = 0

    def boost_speed(self):
        self._speed_vectors[self._degree] = min(self._speed_vectors.get(self._degree, 0) + 0.4, 12.5)

    def reset(self):
        self.x = (self._config['window_width'] - self.width) // 2
        self.y = (self._config['window_height'] - self.height) // 2
        self._speed_vectors = {}
        self._degree = 0

    def update(self):

        if self.boosting: self.boost_speed()
        if self.rotation_factor: self._degree += self.rotation_factor * 7.5

        keys_to_remove = []
        for degree in self._speed_vectors:
            speed = self._speed_vectors[degree]
            self.x += speed * sin(pi / 180 * degree)
            self.y -= speed * cos(pi / 180 * degree)

            self._speed_vectors[degree] -= self._deceleration
            if self._speed_vectors[degree] <= 0:
                keys_to_remove.append(degree)

        for key in keys_to_remove:
            del self._speed_vectors[key]

        self.x = (self.x + self._config['window_width']) % self._config['window_width']
        self.y = (self.y + self._config['window_height']) % self._config['window_height']

    def draw(self, painter: QPainter):

        transform = QTransform()
        transform.translate(self.x, self.y)
        transform.translate(self.width * 0.5, self.height * 0.5)
        transform.rotate(self._degree)
        transform.translate(-self.width * 0.5, -self.height * 0.5)
        painter.setTransform(transform)

        painter.setPen(QPen(QColor(Qt.white), 3))

        painter.drawLine(self.width * 0.5, 0, 0, self.height)
        painter.drawLine(self.width * 0.5, 0, self.width, self.height)
        painter.drawLine(self.width * 0.1, self.height * 0.8, self.width * 0.9, self.height * 0.8)

        if self.boosting and random() < 0.5:
            painter.drawLine(self.width * 0.5, self.height + 10, self.width * 0.3, self.height * 0.8)
            painter.drawLine(self.width * 0.5, self.height + 10, self.width * 0.7, self.height * 0.8)

        painter.setTransform(QTransform())

    @property
    def degree(self):
        return self._degree
