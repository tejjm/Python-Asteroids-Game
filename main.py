import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    pygame.init()
    asteroidfeild = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)

    screen_on = True
    while screen_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0,0,0))
        # player.draw(screen)
        for drawablee in drawable:
            drawablee.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time/1000
        #player.update(dt=dt)
        updatable.update(dt)











if __name__ == "__main__":
    main()
