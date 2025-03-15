import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


update_group = pygame.sprite.Group()
draw_group = pygame.sprite.Group()
asteroids_group = pygame.sprite.Group()

AsteroidField.containers = (update_group,)
Player.containers = (update_group, draw_group)
Asteroid.containers = (asteroids_group, update_group, draw_group)



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       
                return
        screen.fill("black")
        for entity in update_group:
            entity.update(dt)
        for entity in draw_group:
            entity.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    
            

        


if __name__ == "__main__":
    main()