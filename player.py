import pygame
from vars import var

# class player()
var = var()
win = pygame.display.set_mode((var.sizex, var.sizey))

class player():
    def __init__(self, x, y, vel, color):
        self.x = x
        self.y = y
        self.vel = vel
        self.color = color
        self.counter = 0

    # Funktion zum bewegen des linken Spielers
    def moveleft(self):
        if self.counter > 0:
            self.counter -= 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.vel
            # erzeugt Spieleborder
            if self.y < 0:
                self.y = 0
        if keys[pygame.K_s]:
            self.y += self.vel
            # erzeugt Spieleborder
            if self.y > 575:
                self.y = 575
    # Funktion zum bewegen des rechten Spielers.
    def moveright(self):
        if self.counter > 0:
            self.counter -= 1
            print(self.counter)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.vel
            # erzeugt Spieleborder
            if self.y < 0:
                self.y = 0
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            # erzeugt Spieleborder
            if self.y > 575:
                self.y = 575
    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, 20, 100))
