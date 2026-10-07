from shaping import CircleShape
import pygame
import constants
import random
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        self.vector_one = self.velocity.rotate(angle) * 1.2
        self.vector_two = self.velocity.rotate(-angle) * 1.2
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        first_astroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_astroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_astroid.velocity = self.vector_one
        second_astroid.velocity = self.vector_two