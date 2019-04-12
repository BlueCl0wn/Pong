import pygame
from instances import *
import menu

def count_lives():
    global lives_blue
    global lives_green
    # Is the ball right outside of the screen?
    if ball.x >= var.sizex - 20:
        # Has the Player enough lives?
        if lives_blue > 0:
            lives_blue -= 1
            menu.respawn()
        else:
            win.blit(blue_wins, (380, 200))
            menu.restart()
    # Is the ball left outside of the screen?
    elif ball.x <= 0 + 20:
        # Has the Player enough lives?
        if lives_green > 0:
            lives_green -= 1
            menu.respawn()
        else:
            win.blit(green_wins, (380, 200))
            menu.restart()


# def draw():
