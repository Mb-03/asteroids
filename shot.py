import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.position += self.velocity * dt
    

    def draw(self,screend):
        pygame.draw.circle(screend, "white", (int(self.position.x), int(self.position.y)), self.radius, 1)
        
        
        
