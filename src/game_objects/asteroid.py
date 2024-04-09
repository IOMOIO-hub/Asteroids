from yaml import safe_load
from random import uniform, randint

from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.game_objects.game_object import GameObject


class Asteroid(GameObject):
    def __init__(self, rank: int = 3, location: QPoint = None):
        with open('config.yml', 'r') as f:
            self._config = safe_load(f)

        location = location or QPoint(randint(0, self._config['window_width']),
                                      randint(0, self._config['window_height']))
        size = QSize(rank * 40, rank * 40)
        speed = uniform(1.5, 3)
        degree = randint(0, 11) * 30
        super().__init__(location, size, speed, degree)

        self._rank = rank
        self._shape = randint(1, 3)

    def draw(self, painter: QPainter):
        painter.setPen(QColor(Qt.white))
        painter.translate(self.x, self.y)

        painter.drawPolygon({
                                1: [
                                    QPoint(self.width * 0.5, 0),
                                    QPoint(self.width * 0.75, self.height * 0.1),
                                    QPoint(self.width * 0.6, self.height * 0.55),
                                    QPoint(self.width * 0.9, self.height * 0.8),
                                    QPoint(self.width * 0.9, self.height * 0.8),
                                    QPoint(self.width * 0.55, self.height * 0.7),
                                    QPoint(self.width * 0.4, self.height * 0.85),
                                    QPoint(self.width * 0.25, self.height * 0.6),
                                    QPoint(self.width * 0.08, self.height * 0.75),
                                    QPoint(self.width * 0.125, self.height * 0.5),
                                    QPoint(self.width * 0.04, self.height * 0.4),
                                    QPoint(self.width * 0.15, self.height * 0.15)],
                                2: [
                                    QPoint(self.width * 0.25, 0),
                                    QPoint(self.width * 0.85, self.height * 0.15),
                                    QPoint(self.width * 0.9, self.height * 0.9),
                                    QPoint(self.width * 0.55, self.height),
                                    QPoint(self.width * 0.35, self.height * 0.8),
                                    QPoint(self.width * 0.15, self.height * 0.88),
                                    QPoint(self.width * 0.2, self.height * 0.6),
                                    QPoint(0, self.height * 0.25),
                                    QPoint(self.width * 0.3, self.height * 0.45)],
                                3: [
                                    QPoint(self.width, self.height),
                                    QPoint(self.width * 0.15, self.height * 0.95),
                                    QPoint(self.width * 0.075, self.height * 0.6),
                                    QPoint(self.width * 0.25, self.height * 0.45),
                                    QPoint(self.width * 0.2, self.height * 0.15),
                                    QPoint(self.width * 0.5, self.height * 0.03),
                                    QPoint(self.width * 0.45, self.height * 0.35),
                                    QPoint(self.width * 0.75, self.height * 0.2),
                                    QPoint(self.width * 0.9, self.height * 0.48),
                                    QPoint(self.width, self.height * 0.55),
                                    QPoint(self.width * 0.8, self.height * 0.8)]
                            }[self._shape])

        painter.translate(-self.x, -self.y)

    @property
    def rank(self):
        return self._rank
