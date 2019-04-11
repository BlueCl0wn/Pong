import pygame
from random import choice
from instances import *

# Funktion die ueberprueft ob die Escape Taste fuer Pausemenu gedrueckt wurde.
def pauseupdate():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        if var.counter == 0:
            var.pause = var.pause * -1
            var.counter += 10

# Funktion die das Bild für die Pause einfuegt wenn var pause 1 ist.
def pausemenu():
    global pause
    if var.pause == 1:
        win.blit(pauseimg, (380, 200))

def restart():
        ball.vel_list = [-6, -5, -4, -3, 3, 4, 5, 6]
        ball.velx = choice(ball.vel_list)
        ball.vely = choice(ball.vel_list)
        ball.x = 600
        ball.y = 336
        var.pause = var.pause * -1
