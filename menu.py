import pygame
from random import choice
from instances import *

# Funktion die ueberprueft ob die Escape Taste fuer Pausemenu gedrueckt wurde.
def pauseupdate():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        if var.pausecounter == 0:
            var.pause = var.pause * -1
            var.pausecounter += 10

# Funktion die das Bild für die Pause einfuegt wenn var pause 1 ist.
def pausemenu():
    global pause
    if var.pause == 1:
        win.blit(pauseimg, (380, 200))

def varpause():
    var.pause = var.pause * -1

# def countdown()

def respawn():
        ball.velx = choice(ball.vel_list)
        ball.vely = choice(ball.vel_list)
        ball.x = 600
        ball.y = 336
        # countdown()

def restart():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        lives_blue = 3
        lives_green = 3
        respawn()

def mainrestart():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        lives_blue = 3
        lives_green = 3
        respawn()
        varpause()
