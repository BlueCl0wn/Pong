import pygame
from random import randint
import time

pygame.init()


# Öffnen von Images
pauseimg = pygame.image.load("pause.png")

# Spielefenster wird erstellt und weitere Nebeneinstellungen
sizex = 1200
sizey = 675
win = pygame.display.set_mode((sizex, sizey))
pygame.display.set_caption("Pong")

# Klasse Ball mit der der Ball definiert wird
class ball():
    def __init__(self, color=(255, 0 ,0)):
        self.velx = randint(-6,6)
        self.vely = randint(-6,6)
        self.x = 600
        self.y = 336
        self.move = 0
        self.color = color
    def moveball(self):
        self.x += self.velx
        self.y += self.vely
        if self.y > (sizey-20) or self.y < (0+20):
            self.vely = self.vely * -1
    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), 20, 0)
    # def count(self):
    #     if count == 150:
    #         self.move = 1

# Klasse Player mit der die beiden Spieler definiert werden.
class player():
    def __init__(self, x, y, vel, color):
        self.x = x
        self.y = y
        self.vel = vel
        self.color = color

    # Funktion zum bewegen des linken Spielers
    def moveleft(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.vel
            # erzeugt Spieleborder
            if self.y < 0:
                self.y = 0
        if keys[pygame.K_s]:
            self.y += self.vel
            # erzeugt Spieleborder
            if self.y > 575:
                self.y = 575
    # Funktion zum bewegen des rechten Spielers.
    def moveright(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.vel
            # erzeugt Spieleborder
            if self.y < 0:
                self.y = 0
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            # erzeugt Spieleborder
            if self.y > 575:
                self.y = 575
    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, 20, 100))

def colllide():
    # Es wird überprüft ob der __linke__ Spieler berührt wird, wenn ja wird der Balla abgestoßen.
    if ball.velx < 0:
        # Es wird überprüft ob der Ball auf der gleichen y-Höhe ist wie der linke Spieler.
        if ball.y >= pl_left.y and ball.y <= (pl_left.y + 100):
            # Es wird überprüft ob der Bal auf der gleichen x-Höhe sit wie der linke Spieler.
            if ball.x <= 60:
                ball.x = 60
                ball.velx = ball.velx * -1
    # Es wird überprüft ob der __rechte__ Spieler berührt wird, wenn ja wird der Balla abgestoßen.
    elif ball.velx > 0:
        # Es wird überprüft ob der Ball auf der gleichen y-Höhe ist wie der rechte Spieler.
        if ball.y >= pl_right.y and ball.y <= (pl_right.y + 100):
            # Es wird überprüft ob der Bal auf der gleichen x-Höhe sit wie der linke Spieler.
            if ball.x >= 1140:
                ball.x = 1140
                ball.velx = ball.velx * -1

pause = -1
# Funktion die über ob die Escape Taste für Pausemenu gedrückt wurde.
def pauseupdate():
    global pause
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pause = pause * -1

# Funktion die das Bild für die Pause einfügt wenn var pause 1 ist.
def pausemenu():
    global pause
    if pause == 1:
        win.blit(pauseimg, (421, 219))



# Instanzen des Balles und der Spieler werden erstellt.
pl_left = player(x=20, y=300, vel=6, color=(0, 255, 0))
pl_right = player(x=1160, y=300, vel=6, color=(0, 0, 255))
ball = ball()
# Main-Loop
run = 1
while run:
    pygame.time.delay(30)

    # Es wird überprüft ob das Spiel geschlossen werden soll.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0

    pauseupdate()
    if pause == 1:
        pausemenu()
    elif pause == -1:
        # Füllen des Spielefensters.
        win.fill((255, 255, 255))

        # Funktionen zum Bewegen der Instanzen.
        pl_left.moveleft()
        pl_right.moveright()
        ball.moveball()

        colllide()

        # Instanzen werden gezeichnet.
        pl_left.draw()
        pl_right.draw()
        ball.draw()

    pygame.display.update()

pygame.quit()
