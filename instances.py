import pygame
import player
import ball
from vars import var

# Instanzen werden erstellt.
pl_left = player.player(x=20, y=300, vel=6, color=(0, 255, 0))
pl_right = player.player(x=1160, y=300, vel=6, color=(0, 0, 255))
ball = ball.ball()
var = var()
win = pygame.display.set_mode((var.sizex, var.sizey))

# Oeffnen von Images
pauseimg = pygame.image.load("images/pause.png")
green_heart = pygame.image.load("images/green_heart.png")
red_heart = pygame.image.load("images/red_heart.png")
