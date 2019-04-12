import pygame
from random import choice
from vars import var

var = var()
win = pygame.display.set_mode((var.sizex, var.sizey))
# class Ball
class ball():
    def __init__(self, color=(255, 0 ,0)):
        self.vel_list = [-6, -5, -4, 4, 5, 6]
        self.velx = choice(self.vel_list)
        self.vely = choice(self.vel_list)
        self.x = 600
        self.y = 336
        self.move = 0
        self.color = color
        self.radius = 20
    def moveball(self):
        self.x += self.velx
        self.y += self.vely
        if self.y > (var.sizey - self.radius) or self.y < (0 + self.radius):
            self.vely = self.vely * -1
    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius, 0)
