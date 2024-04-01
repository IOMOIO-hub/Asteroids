from src import config

import math
from random import uniform, randint, choice

from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.game_objects.game_object import GameObject


class Asteroid(GameObject):
    def __init__(self, rank: int):
        location = QPoint(randint(120, config.WINDOW_WIDTH - 120), randint(120, config.WINDOW_HEIGHT - 120))

        if rank == 1: size = QSize(40, 40)
        elif rank == 2: size = QSize(80, 80)
        else: size = QSize(120, 120)

        super().__init__(location, size)

        self.speed = uniform(1.5, 4)
        self.degree = choice([degree for degree in range(0, 360, 30)])
        self.image = choice([image for image in range(1, 4)])

    def update(self):
        self.location.setX(int(self.location.x() + self.speed * math.sin(math.pi / 180 * self.degree)))
        self.location.setY(int(self.location.y() - self.speed * math.cos(math.pi / 180 * self.degree)))

        self.location.setX((self.location.x() + config.WINDOW_WIDTH) % config.WINDOW_WIDTH)
        self.location.setY((self.location.y() + config.WINDOW_HEIGHT) % config.WINDOW_HEIGHT)

    def draw_asteroid_1(self, painter: QPainter, height, width):
        painter.drawLine(width * 0.5, 0, width * 0.75, height * 0.1)
        painter.drawLine(width * 0.75, height * 0.1, width * 0.6, height * 0.55)
        painter.drawLine(width * 0.6, height * 0.55, width * 0.9, height * 0.8)
        painter.drawLine(width * 0.9, height * 0.8, width * 0.55, height * 0.7)
        painter.drawLine(width * 0.55, height * 0.7, width * 0.4, height * 0.85)
        painter.drawLine(width * 0.4, height * 0.85, width * 0.25, height * 0.6)
        painter.drawLine(width * 0.25, height * 0.6, width * 0.08, height * 0.75)
        painter.drawLine(width * 0.08, height * 0.75, width * 0.125, height * 0.5)
        painter.drawLine(width * 0.125, height * 0.5, width * 0.04, height * 0.4)
        painter.drawLine(width * 0.04, height * 0.4, width * 0.15, height * 0.15)
        painter.drawLine(width * 0.15, height * 0.15, width * 0.5, 0)

    def draw_asteroid_2(self, painter: QPainter, height, width):
        painter.drawLine(width * 0.25, 0, width * 0.85, height * 0.15)
        painter.drawLine(width * 0.85, height * 0.15, width * 0.9, height * 0.9)
        painter.drawLine(width * 0.9, height * 0.9, width * 0.55, height)
        painter.drawLine(width * 0.55, height, width * 0.35, height * 0.8)
        painter.drawLine(width * 0.35, height * 0.8, width * 0.15, height * 0.88)
        painter.drawLine(width * 0.15, height * 0.88, width * 0.2, height * 0.6)
        painter.drawLine(width * 0.2, height * 0.6, 0, height * 0.25)
        painter.drawLine(0, height * 0.25, width * 0.3, height * 0.45)
        painter.drawLine(width * 0.3, height * 0.45, width * 0.25, 0)

    def draw_asteroid_3(self, painter: QPainter, height, width):
        painter.drawLine(width, height, width * 0.15, height * 0.95)
        painter.drawLine(width * 0.15, height * 0.95, width * 0.075, height * 0.6)
        painter.drawLine(width * 0.075, height * 0.6, width * 0.25, height * 0.45)
        painter.drawLine(width * 0.25, height * 0.45, width * 0.2, height * 0.15)
        painter.drawLine(width * 0.2, height * 0.15, width * 0.5, height * 0.03)
        painter.drawLine(width * 0.5, height * 0.03, width * 0.45, height * 0.35)
        painter.drawLine(width * 0.45, height * 0.35, width * 0.75, height * 0.2)
        painter.drawLine(width * 0.75, height * 0.2, width * 0.9, height * 0.48)
        painter.drawLine(width * 0.9, height * 0.48, width, height * 0.55)
        painter.drawLine(width, height * 0.55, width * 0.8, height * 0.8)
        painter.drawLine(width * 0.8, height * 0.8, width, height)

    def draw(self, painter: QPainter):
        height = self.size.height()
        width = self.size.width()

        painter.setPen(QColor(Qt.white))
        painter.translate(self.location.x(), self.location.y())

        if self.image == 1: self.draw_asteroid_1(painter, height, width)
        if self.image == 2: self.draw_asteroid_2(painter, height, width)
        if self.image == 3: self.draw_asteroid_3(painter, height, width)

        painter.translate(-self.location.x(), -self.location.y())

