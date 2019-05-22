from instances import *

def colllide():
    # Es wird ueberprueft ob der linke Spieler beruehrt wird, wenn ja wird der Ball abgestossen.
    if ball.velx < (0): # <--

        # Es wird ueberprueft ob der Ball auf der gleichen y-Hoehe ist wie der linke Spieler.
        if ball.y >= (pl_left.y - ball.radius) and ball.y <= (pl_left.y + pl_left.height + ball.radius):
            # Es wird ueberprueft ob der Ball auf der gleichen x Hoehe ist wie der linke Spieler.
            if ball.x <= (pl_left.x + pl_left.width + ball.radius) and ball.x >= (pl_left.x + pl_left.width + ball.radius - 9):
                ball.x = pl_left.x + pl_left.width + ball.radius
                # Flugrichtung x wird umgedreht.
                ball.velx = ball.velx * -1

        if ball.x >= (pl_left.x) and ball.x <= (pl_left.x + pl_left.width):
            if pl_left.counter == (0):
                if ball.y >= (pl_left.y - ball.radius) and  ball.y <= (pl_left.y - ball.radius + 9):
                    ball.y = (pl_left.y - ball.radius)
                    ball.vely *= -1
                    # Flugrichtung y wird umgedreht.
                    pl_left.counter += 500
                    # counter gegen Bugs wird hochgesetzt.
                if ball.y >= (pl_left.y + pl_left.height + ball.radius - 7) and ball.y < (pl_left.y + pl_left.height + ball.radius):
                    ball.y = (pl_left.y + pl_left.height + ball.radius)
                    # Flugrichtung y wird umgedreht.
                    ball.vely *= -1
                    # counter gegen Bugs wird hochgesetzt.
                    pl_left.counter += 500

    # Es wird ueberprueft ob der rechte Spieler beruehrt wird, wenn ja wird der Ball abgestossen.
    elif ball.velx > (0): # -->

        # Es wird ueberprueft ob der Ball auf der gleichen y Hoehe ist wie der rechte Spieler.
        if ball.y >= (pl_right.y - ball.radius) and ball.y <= (pl_right.y + pl_right.height + ball.radius):
            # Es wird ueberprueft ob der Ball auf der gleichen x Hoehe ist wie der rechte Spieler.
            if ball.x > (pl_right.x - ball.radius) and ball.x <= (pl_right.x - ball.radius + 9):
                ball.x = pl_right.x - ball.radius
                ball.velx *= -1

        if ball.x >= (pl_right.x) and ball.x <= (pl_right.x + pl_right.width):
            if pl_right.counter == 0:
                # pl_right oben
                if ball.y > (pl_right.y - ball.radius) and  ball.y <= (pl_right.y - ball.radius + 9):
                    ball.y = (pl_right.y - ball.radius)
                    ball.vely *= -1
                    pl_right.counter += 500
                # pl_right unten
                if ball.y >= (pl_right.y + pl_right.height + ball.radius - 9) and ball.y < (pl_right.y + pl_right.height + ball.radius):
                    ball.y = (pl_right.y + pl_right.height + ball.radius)
                    ball.vely *= -1
                    pl_right.counter += 500
