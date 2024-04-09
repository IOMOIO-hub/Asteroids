from abc import ABC, abstractmethod
from math import sin, cos, pi
from yaml import safe_load

from PyQt5.QtGui import *
from PyQt5.QtCore import *


class GameObject(ABC):
    def __init__(self, location: QPoint, size: QSize, speed: float = 0, degree: int = 0):
        self._location = location
        self._size = size

        self._speed = speed
        self._degree = degree

        with open('config.yml', 'r') as f:
            self._config = safe_load(f)

    def update(self):
        self.x += self._speed * sin(pi / 180 * self._degree)
        self.y -= self._speed * cos(pi / 180 * self._degree)

        self.x = (self.x + self._config['window_width']) % self._config['window_width']
        self.y = (self.y + self._config['window_height']) % self._config['window_height']

    @abstractmethod
    def draw(self, painter: QPainter) -> None:
        raise NotImplementedError

    def is_collide(self, other) -> bool:
        return (self.x < other.x + other.width and self.x + self.width > other.x and
                self.y < other.y + other.height and self.y + self.height > other.y)

    @property
    def x(self):
        return self._location.x()

    @property
    def y(self):
        return self._location.y()

    @x.setter
    def x(self, value: float):
        self._location.setX(value)

    @y.setter
    def y(self, value: float):
        self._location.setY(value)

    @property
    def width(self):
        return self._size.width()

    @property
    def height(self):
        return self._size.height()
