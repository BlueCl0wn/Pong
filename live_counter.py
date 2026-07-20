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
        var.score_screen = 1  # Show score screen
        pygame.time.delay(500)  # Small delay to ensure the screen updates

    # Is the ball left outside of the screen?
    elif ball.x <= 0:
        goal_green += 1
        var.score_screen = 1  # Show score screen
        pygame.time.delay(500)  # Small delay to ensure the screen updates


def draw(goal_blue, goal_green):
    pass
