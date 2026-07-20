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

# Funktion für den Score-Bildschirm
def score_screen():
    if var.score_screen == 1:
        # Halbdurchsichtiger Hintergrund
        overlay = pygame.Surface((var.sizex, var.sizey))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(180)
        win.blit(overlay, (0, 0))
        
        # Anzeige des aktuellen Standes
        score_text = font.render(f"{goal_green} - {goal_blue}", True, (255, 255, 255))
        win.blit(score_text, (var.sizex // 2 - score_text.get_width() // 2, var.sizey // 2 - 50))
        
        # Anzeige einer Nachricht
        message = small_font.render("Press SPACE to continue", True, (255, 255, 255))
        win.blit(message, (var.sizex // 2 - message.get_width() // 2, var.sizey // 2 + 20))
        
        # Überprüfe, ob die Leertaste gedrückt wurde
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            var.score_screen = 0
            respawn()
            pygame.time.delay(200)  # Verhindere mehrfaches Auslösen

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
