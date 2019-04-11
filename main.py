import pygame
import time
from instances import *
import collide
import menu

pygame.init()
# Spielefenster wird erstellt und weitere Nebeneinstellungen
pygame.display.set_caption("Pong")


# Main Loop
while var.run:
    pygame.time.delay(30)
    if var.counter > 0:
        var.counter -= 1
    # Es wird ueberprueft ob das Spiel geschlossen werden soll.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var.run = 0

    menu.pauseupdate()
    if var.pause == 1:
        menu.pausemenu()
        menu.restart()
    elif var.pause == -1:
        # Fuellen des Spielefensters.
        win.fill((255, 255, 255))

        # Funktionen zum Bewegen der Instanzen.
        pl_left.moveleft()
        pl_right.moveright()
        ball.moveball()

        collide.colllide()

        # Instanzen werden gezeichnet.
        pl_left.draw()
        pl_right.draw()
        ball.draw()

    pygame.display.update()

pygame.quit()
