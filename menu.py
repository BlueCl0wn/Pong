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

# Funktion die das Bild für die Pause einfügt und die Punkte anzeigt, wenn var pause 1 ist.
def pausemenu():
    global pause
    if var.pause == 1:
        win.blit(pauseimg, (380, 200))
        
        # Anzeige der Punkte
        score_text = font.render(f"{goal_green} - {goal_blue}", True, (0, 0, 0))
        win.blit(score_text, (var.sizex // 2 - score_text.get_width() // 2, 300))

def varpause():
    var.pause = var.pause * -1

# def countdown()

def respawn():
    ball.vel_list = [-6, -5, -4, -3, 3, 4, 5, 6]
    ball.velx = choice(ball.vel_list)
    ball.vely = choice(ball.vel_list)
    ball.x = 600
    ball.y = 336
    pygame.time.delay(1000)
    # countdown()

def restart():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        goal_blue = 0
        goal_green = 0
        respawn()

def mainrestart():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        goal_blue = 0
        goal_green = 0
        respawn()
        varpause()
