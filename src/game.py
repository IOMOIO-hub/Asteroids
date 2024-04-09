from yaml import safe_load

from math import sin, cos, pi

from PyQt5.QtCore import *
from PyQt5.QtGui import *

from game_objects.spaceship import Spaceship
from game_objects.asteroid import Asteroid
from game_objects.bullet import Bullet


class Game:
    def __init__(self):
        self._spaceship = Spaceship()
        self._asteroids = [Asteroid() for _ in range(4)]
        self._bullets = []

        self._score = 0
        self._lives = 3

        with open('config.yml', 'r') as f:
            self._config = safe_load(f)

    def update(self):
        self._spaceship.update()

        asteroids_to_destroy = set()
        for asteroid in self._asteroids:
            asteroid.update()

            if not self._spaceship.is_collide(asteroid):
                continue

            self._lives -= 1
            if self._lives == 0:
                return self.restart()
            self._spaceship.reset()
            asteroids_to_destroy.add(asteroid)

        bullets_to_remove = set()
        for bullet in self._bullets:
            bullet.update()

            if bullet.is_out_of_view():
                bullets_to_remove.add(bullet)

            for asteroid in self._asteroids:
                if bullet.is_collide(asteroid):
                    bullets_to_remove.add(bullet)
                    asteroids_to_destroy.add(asteroid)

        for asteroid in asteroids_to_destroy:
            self.destroy_asteroid(asteroid)
        for bullet in bullets_to_remove:
            self._bullets.remove(bullet)

    def destroy_asteroid(self, asteroid: Asteroid):
        self._asteroids.remove(asteroid)
        self._score += {1: 100, 2: 50, 3: 20}[asteroid.rank]
        if asteroid.rank > 1:
            self._asteroids.append(Asteroid(asteroid.rank - 1, QPoint(asteroid.x, asteroid.y)))
            self._asteroids.append(Asteroid(asteroid.rank - 1, QPoint(asteroid.x, asteroid.y)))

    def draw(self, painter: QPainter):
        painter.fillRect(0, 0, self._config['window_width'], self._config['window_height'], QBrush(Qt.SolidPattern))

        self._spaceship.draw(painter)

        for asteroid in self._asteroids:
            asteroid.draw(painter)

        for bullet in self._bullets:
            bullet.draw(painter)

        painter.setPen(QColor(Qt.white))
        painter.setFont(QFont('Courier New', 24))
        painter.drawText(10, 60, str(self._score))
        painter.drawText(10, 100, "A" * self._lives)

    def start_boosting(self):
        self._spaceship.boosting = True

    def stop_boosting(self):
        self._spaceship.boosting = False

    def start_rotation_to_right(self):
        self._spaceship.rotation_factor = 1

    def start_rotation_to_left(self):
        self._spaceship.rotation_factor = -1

    def stop_rotation(self):
        self._spaceship.rotation_factor = 0

    def shoot(self):

        if len(self._bullets) > 8:
            return

        new_bullet_x = self._spaceship.x + (1 + sin(pi / 180 * self._spaceship.degree)) * (self._spaceship.width // 2)
        new_bullet_y = self._spaceship.y + (1 - cos(pi / 180 * self._spaceship.degree)) * (self._spaceship.height // 2)
        self._bullets.append(Bullet(QPoint(new_bullet_x, new_bullet_y), self._spaceship.degree))

    def restart(self):
        self.__init__()
