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

lives_blue = 3
lives_green = 3

# Oeffnen von Images
pauseimg = pygame.image.load("images/pause.png")
green_heart = pygame.image.load("images/green_heart.png")
blue_heart = pygame.image.load("images/blue_heart.png")
green_wins = pygame.image.load("images/green_wins.png")
blue_wins = pygame.image.load("images/blue_wins.png")
