import pygame
from instances import green_heart
from instances import red_heart
import menu


lives_right = 3
lives_left = 3
def count_lives():
    # Ist der Ball rechts ausserhalb des Bildschirms?
    if ball.x == var.sizex - 20:
        # Hat Spiler rechts noch ein Leben?
            if lives_right > 0:
                menu.restart()
            else:
                



def draw():
