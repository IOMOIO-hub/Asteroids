from src import config

from random import uniform, randint

from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.game_objects.game_object import GameObject


class Asteroid(GameObject):
    def __init__(self, rank: int = 3, location: QPoint = None):
        location = location or QPoint(randint(0, config.WINDOW_WIDTH), randint(0, config.WINDOW_HEIGHT))
        size = QSize(rank * 40, rank * 40)
        speed = uniform(1.5, 3)
        degree = randint(0, 11) * 30
        super().__init__(location, size, speed, degree)

        self.rank = rank
        self.shape = randint(1, 3)

    def draw(self, painter: QPainter):
        painter.setPen(QColor(Qt.white))
        painter.translate(self.location.x(), self.location.y())

        width = self.size.width()
        height = self.size.height()

        painter.drawPolygon({
            1: [
                QPoint(width * 0.5, 0), QPoint(width * 0.75, height * 0.1),
                QPoint(width * 0.6, height * 0.55), QPoint(width * 0.9, height * 0.8),
                QPoint(width * 0.9, height * 0.8), QPoint(width * 0.55, height * 0.7),
                QPoint(width * 0.4, height * 0.85), QPoint(width * 0.25, height * 0.6),
                QPoint(width * 0.08, height * 0.75), QPoint(width * 0.125, height * 0.5),
                QPoint(width * 0.04, height * 0.4), QPoint(width * 0.15, height * 0.15)],
            2: [
                QPoint(width * 0.25, 0), QPoint(width * 0.85, height * 0.15),
                QPoint(width * 0.9, height * 0.9), QPoint(width * 0.55, height),
                QPoint(width * 0.35, height * 0.8), QPoint(width * 0.15, height * 0.88),
                QPoint(width * 0.2, height * 0.6), QPoint(0, height * 0.25),
                QPoint(width * 0.3, height * 0.45)],
            3: [
                QPoint(width, height), QPoint(width * 0.15, height * 0.95),
                QPoint(width * 0.075, height * 0.6), QPoint(width * 0.25, height * 0.45),
                QPoint(width * 0.2, height * 0.15), QPoint(width * 0.5, height * 0.03),
                QPoint(width * 0.45, height * 0.35), QPoint(width * 0.75, height * 0.2),
                QPoint(width * 0.9, height * 0.48), QPoint(width, height * 0.55),
                QPoint(width * 0.8, height * 0.8)]
        }[self.shape])

        painter.translate(-self.location.x(), -self.location.y())

    def __repr__(self):
        return f"({self.rank}, {self.speed.__round__(2)}, {self.degree})"
