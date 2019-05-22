import pygame
import player
import ball
from vars import var

# Instanzen werden erstellt.
pl_left = player.player(x=40, y=300, vel=8, color=(0, 255, 0))
pl_right = player.player(x=1140, y=300, vel=8, color=(0, 0, 255))
ball = ball.ball()
var = var()
win = pygame.display.set_mode((var.sizex, var.sizey))

goal_blue = 0
goal_green = 0

# Oeffnen von Images
pauseimg = pygame.image.load("images/pause.png")
