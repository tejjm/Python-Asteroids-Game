import pygame
from constants import *
from player import Player
def main():
    pygame.init()
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
        player.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time/1000
        player.update(dt=dt)












if __name__ == "__main__":
    main()
