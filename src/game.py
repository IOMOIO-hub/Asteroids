import math

import config

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from game_objects.spaceship import Spaceship
from game_objects.asteroid import Asteroid
from game_objects.bullet import Bullet


class Game:
    def __init__(self):
        self.spaceship = Spaceship()
        self.asteroids = [Asteroid() for _ in range(4)]
        self.bullets = []

        self.score = 0
        self.lives = 3

    def update(self):
        self.spaceship.update()

        asteroids_to_destroy = []
        for asteroid in self.asteroids:
            asteroid.update()

            if not self.spaceship.isCollide(asteroid):
                continue

            self.lives -= 1
            if self.lives == 0:
                return self.restart()
            self.spaceship.reset()
            asteroids_to_destroy.append(asteroid)

        for bullet in self.bullets:
            bullet.update()
            if bullet.isOutOfView():
                self.bullets.remove(bullet)

            for asteroid in self.asteroids:
                if bullet.isCollide(asteroid):
                    self.bullets.remove(bullet)
                    asteroids_to_destroy.append(asteroid)

        for asteroid in asteroids_to_destroy:
            self.destroyAsteroid(asteroid)

    def destroyAsteroid(self, asteroid: Asteroid):
        self.asteroids.remove(asteroid)
        self.score += {1: 100, 2: 50, 3: 20}[asteroid.rank]
        if asteroid.rank > 1:
            self.asteroids.append(Asteroid(asteroid.rank - 1, QPoint(asteroid.location)))
            self.asteroids.append(Asteroid(asteroid.rank - 1, QPoint(asteroid.location)))

    def draw(self, painter: QPainter):
        painter.fillRect(0, 0, config.WINDOW_WIDTH, config.WINDOW_HEIGHT, QBrush(Qt.SolidPattern))
        self.spaceship.draw(painter)
        for asteroid in self.asteroids:
            asteroid.draw(painter)
        for bullet in self.bullets:
            bullet.draw(painter)

        painter.setPen(QColor(Qt.white))
        painter.setFont(QFont('Courier New', 24))
        painter.drawText(10, 60, str(self.score))
        painter.drawText(10, 100, "A" * self.lives)

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

    def shoot(self):
        new_bullet_x = self.spaceship.location.x() + (1 + math.sin(math.pi / 180 * self.spaceship.degree)) * (
                self.spaceship.size.width() // 2)
        new_bullet_y = self.spaceship.location.y() + (1 - math.cos(math.pi / 180 * self.spaceship.degree)) * (
                self.spaceship.size.height() // 2)
        self.bullets.append(Bullet(QPoint(int(new_bullet_x), int(new_bullet_y)), self.spaceship.degree))

    def restart(self):
        self.__init__()
