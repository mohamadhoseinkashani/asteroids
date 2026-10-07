import pygame
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS
import shaping
from shot import Shot



class Player(shaping.CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.cool_down_timer = 0
        
        
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt: float) -> None:
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_SPACE] and self.cool_down_timer <= 0:
            self.shoot()
        else:
            self.cool_down_timer -= dt

        
    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        self.bullet = Shot(self.position.x, self.position.y)
        self.bullet.velocity = pygame.Vector2(0, 6).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.cool_down_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

