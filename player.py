import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED,PLAYER_SPEED,PLAYER_SHOOT_SPEED,SHOT_RADIUS,PLAYER_SHOOT_COOLDOWN
class Player(CircleShape):
    def __init__(self,x,y):
        self.timer = 0
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(surface=screen,color=(255,255,255),points=self.triangle(),width=2)
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED *dt
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN
            self.timer -= dt

            
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    # python
    def shoot(self):
        from shot import Shot
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        muzzle = self.position + forward * (self.radius + SHOT_RADIUS + 2)
        shot = Shot(muzzle.x, muzzle.y)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        