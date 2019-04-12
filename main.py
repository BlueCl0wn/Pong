import pygame
import time
from instances import *
import collide
import menu
import live_counter
# import live_counter

pygame.init()
# Spielefenster wird erstellt und weitere Nebeneinstellungen
pygame.display.set_caption("Pong")


# Main Loop
while var.run:
    pygame.time.delay(30)
    if var.pausecounter > 0:
        var.pausecounter -= 1
    # Es wird ueberprueft ob das Spiel geschlossen werden soll.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var.run = 0

    menu.pauseupdate()
    if var.pause == 1:
        menu.pausemenu()
        if var.pause == 1: # pausemenu active
            menu.mainrestart()
    elif var.pause == -1: # pausemenu negative
        # Fuellen des Spielefensters.
        win.fill((255, 255, 255))

        # Funktionen zum Bewegen der Instanzen.
        pl_left.moveleft()
        pl_right.moveright()
        ball.moveball()

        # Funktion zum ueberpruefen ob der Ball einen der Spieler berührt.
        collide.colllide()

        # Funktion die die Leben der Spieler zaehlt.
        live_counter.count_lives()
        # Instanzen werden gezeichnet.
        pl_left.draw()
        pl_right.draw()
        ball.draw()

    pygame.display.update()

pygame.quit()
