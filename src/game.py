import math

from yaml import safe_load

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

        with open('config.yml', 'r') as f:
            self.config = safe_load(f)

    def update(self):
        self.spaceship.update()

        asteroids_to_destroy = set()
        for asteroid in self.asteroids:
            asteroid.update()

            if not self.spaceship.is_collide(asteroid):
                continue

            self.lives -= 1
            if self.lives == 0:
                return self.restart()
            self.spaceship.reset()
            asteroids_to_destroy.add(asteroid)

        bullets_to_remove = set()
        for bullet in self.bullets:
            bullet.update()
            if bullet.is_out_of_view():
                bullets_to_remove.add(bullet)

            for asteroid in self.asteroids:
                if bullet.is_collide(asteroid):
                    bullets_to_remove.add(bullet)
                    asteroids_to_destroy.add(asteroid)

        for asteroid in asteroids_to_destroy:
            self.destroy_asteroid(asteroid)
        for bullet in bullets_to_remove:
            self.bullets.remove(bullet)

    def destroy_asteroid(self, asteroid: Asteroid):
        self.asteroids.remove(asteroid)
        self.score += {1: 100, 2: 50, 3: 20}[asteroid.rank]
        if asteroid.rank > 1:
            self.asteroids.append(Asteroid(asteroid.rank - 1, QPoint(asteroid.location)))
            self.asteroids.append(Asteroid(asteroid.rank - 1, QPoint(asteroid.location)))

    def draw(self, painter: QPainter):
        painter.fillRect(0, 0, self.config['window_width'], self.config['window_height'], QBrush(Qt.SolidPattern))
        self.spaceship.draw(painter)
        for asteroid in self.asteroids:
            asteroid.draw(painter)
        for bullet in self.bullets:
            bullet.draw(painter)

        painter.setPen(QColor(Qt.white))
        painter.setFont(QFont('Courier New', 24))
        painter.drawText(10, 60, str(self.score))
        painter.drawText(10, 100, "A" * self.lives)

    def start_boosting(self):
        self.spaceship.boosting = True

    def stop_boosting(self):
        self.spaceship.boosting = False

    def start_rotation_to_right(self):
        self.spaceship.rotation_to_right = True
        self.spaceship.rotation_to_left = False

    def start_rotation_to_left(self):
        self.spaceship.rotation_to_right = False
        self.spaceship.rotation_to_left = True

    def stop_rotation(self):
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
