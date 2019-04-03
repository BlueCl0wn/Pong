import pygame
from random import randint
import time

pygame.init()

sizex = 1200
sizey = 675
win = pygame.display.set_mode((sizex, sizey))
pygame.display.set_caption("Pong")

class ball():
    def __init__(self, color=(255, 0 ,0)):
        self.velx = randint(-6,6)
        self.vely = randint(-6,6)
        self.x = 600
        self.y = 336
        self.move = 0
        self.color = color
    def moveball(self):
        self.x += self.velx
        self.y += self.vely
        if self.y > (sizey-20) or self.y < (0+20):
            self.vely = self.vely * -1
    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), 20, 0)
    # def count(self):
    #     if count == 150:
    #         self.move = 1

class player():
    def __init__(self, x, y, vel, color):
        self.x = x
        self.y = y
        self.vel = vel
        self.color = color
    def moveleft(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.vel
            if self.y < 0:
                self.y = 0
        if keys[pygame.K_s]:
            self.y += self.vel
            if self.y > 575:
                self.y = 575
    def moveright(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.vel
            if self.y < 0:
                self.y = 0
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            if self.y > 575:
                self.y = 575
    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, 20, 100))



pl_left = player(x=20, y=300, vel=5, color=(0, 255, 0))
pl_right = player(x=1160, y=300, vel=5, color=(0, 0, 255))

ball = ball()

run = 1
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0

    win.fill((255, 255, 255))

    pl_left.moveleft()
    pl_right.moveright()
    ball.moveball()

    pl_left.draw()
    pl_right.draw()
    ball.draw()

    pygame.display.update()

pygame.quit()
