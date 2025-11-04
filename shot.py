from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS
class Shot(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity = pygame.Vector2()
    def update(self, dt):
        self.position += (self.velocity*dt)
    def draw(self,screen):
        center = (int(self.position.x),int(self.position.y))
        pygame.draw.circle(surface=screen,color=(255,255,255),center=center,radius=SHOT_RADIUS,width=2)