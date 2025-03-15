import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, group=None):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
       
    

    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        else:
            random_angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid1.velocity = vector1 * 1.2
            new_asteroid2.velocity = vector2 * 1.2

            return [new_asteroid1, new_asteroid2]
            
            
            
        

