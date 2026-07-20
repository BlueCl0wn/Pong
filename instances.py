import pygame
import player
import ball
from vars import var

# Initialize pygame if not already initialized
if not pygame.get_init():
    pygame.init()
if not pygame.font.get_init():
    pygame.font.init()

# Instanzen werden erstellt.
pl_left = player.player(x=40, y=300, vel=8, color=(0, 255, 0))
pl_right = player.player(x=1140, y=300, vel=8, color=(0, 0, 255))
ball = ball.ball()
var = var()
win = pygame.display.set_mode((var.sizex, var.sizey))

goal_blue = 0
goal_green = 0

# Schriftarten fr die Anzeige
# Try to use Arial, fall back to default font if not available
try:
    font = pygame.font.SysFont('Arial', 40)
except:
    font = pygame.font.Font(None, 40)

try:
    small_font = pygame.font.SysFont('Arial', 24)
except:
    small_font = pygame.font.Font(None, 24)

# Oeffnen von Images
try:
    pauseimg = pygame.image.load("images/pause.png")
except:
    # Create a placeholder surface if image can't be loaded
    pauseimg = pygame.Surface((100, 100))
    pauseimg.fill((200, 200, 200))
