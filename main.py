import pygame
from random import choice
import time
import ball
import player
from vars import var
import collide

pygame.init()
var = var()
# Öffnen von Images
pauseimg = pygame.image.load("pause.png")

# Spielefenster wird erstellt und weitere Nebeneinstellungen
win = pygame.display.set_mode((var.sizex, var.sizey))
pygame.display.set_caption("Pong")

# Funktion die über ob die Escape Taste für Pausemenu gedrückt wurde.
def pauseupdate():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        if var.counter == 0:
            var.pause = var.pause * -1
            var.counter += 10

# Funktion die das Bild für die Pause einfügt wenn var pause 1 ist.
def pausemenu():
    global pause
    if var.pause == 1:
        win.blit(pauseimg, (380, 200))

def restart():
    if var.pause == 1:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            ball.vel_list = [-6, -5, -4, -3, 3, 4, 5, 6]
            ball.velx = choice(ball.vel_list)
            ball.vely = choice(ball.vel_list)
            ball.x = 600
            ball.y = 336
            var.pause = var.pause * -1

# Instanzen des Balles und der Spieler werden erstellt.
pl_left = player.player(x=20, y=300, vel=6, color=(0, 255, 0))
pl_right = player.player(x=1160, y=300, vel=6, color=(0, 0, 255))
ball = ball.ball()

# Main-Loop
while var.run:
    pygame.time.delay(30)
    if var.counter > 0:
        var.counter -= 1
    # Es wird überprüft ob das Spiel geschlossen werden soll.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var.run = 0

    pauseupdate()
    if var.pause == 1:
        pausemenu()
        restart()
    elif var.pause == -1:
        # Füllen des Spielefensters.
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
