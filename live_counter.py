import pygame
from instances import *
import menu

def count_goals():
    global goal_blue
    global goal_green
    # Is the ball right outside of the screen?
    if ball.x >= var.sizex:
        # Has the Player enough lives?
        goal_blue += 1
        menu.respawn()

    # Is the ball left outside of the screen?
    elif ball.x <= 0:
        goal_green += 1
        menu.respawn()


def draw(goal_blue, goal_green):
    pass
