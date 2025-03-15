import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
    

    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    

    def update(self, dt):
        self.position += (self.velocity * dt)

