import config

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from game_objects.spaceship import Spaceship


class Game:
    def __init__(self):
        self.spaceship = Spaceship(
            QPoint((config.WINDOW_WIDTH - 45) // 2, (config.WINDOW_HEIGHT - 60) // 2),
            QSize(45, 60)
        )

    def update(self):
        self.spaceship.update()

    def draw(self, painter: QPainter):
        painter.fillRect(0, 0, config.WINDOW_WIDTH, config.WINDOW_HEIGHT, QBrush(Qt.SolidPattern))
        self.spaceship.draw(painter)

    def startBoosting(self):
        self.spaceship.boosting = True

    def stopBoosting(self):
        self.spaceship.boosting = False

    def startRotationToRight(self):
        self.spaceship.rotation_to_right = True
        self.spaceship.rotation_to_left = False

    def startRotationToLeft(self):
        self.spaceship.rotation_to_right = False
        self.spaceship.rotation_to_left = True

    def stopRotation(self):
        self.spaceship.rotation_to_right = False
        self.spaceship.rotation_to_left = False

    def startShooting(self):
        self.spaceship.shooting = True

    def stopShooting(self):
        self.spaceship.shooting = False
