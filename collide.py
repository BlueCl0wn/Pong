from instances import *

def colllide():
    # Es wird ueberprueft ob der linke Spieler beruehrt wird, wenn ja wird der Ball abgestossen.
    if ball.velx < 0:
        # Es wird ueberprueft ob der Ball auf der gleichen y-Hoehe ist wie der linke Spieler.
        if ball.y >= (pl_left.y - 20) and ball.y <= (pl_left.y + 120):
            # Es wird ueberprueft ob der Ball auf der gleichen x Hoehe ist wie der linke Spieler.
            if ball.x <= 60 and ball.x >= 54:
                ball.x = 60
                # Flugrichtung x wird umgedreht.
                ball.velx = ball.velx * -1
        if ball.x >= 10 and ball.x <= 50:
            if pl_left.counter == 0:
                if ball.y >= (pl_left.y - 20) and  ball.y <= (pl_left.y - 20 + 6):
                    ball.y = (pl_left.y - 20)
                    ball.vely = ball.vely * -1
                    # Flugrichtung y wird umgedreht.
                    pl_left.counter += 500
                    # counter gegen Bugs wird hochgesetzt.
                if ball.y >= (pl_left.y + 100 + 20) and ball.y < (pl_left.y + 100 + 20):
                    ball.y = (pl_left.y + 100 + 20)
                    # Flugrichtung y wird umgedreht.
                    ball.vely = ball.vely * -1
                    # counter gegen Bugs wird hochgesetzt.
                    pl_left.counter += 500
    # Es wird ueberprueft ob der rechte Spieler beruehrt wird, wenn ja wird der Ball abgestossen.
    elif ball.velx > 0:
        # Es wird ueberprueft ob der Ball auf der gleichen y Hoehe ist wie der rechte Spieler.
        if ball.y >= (pl_right.y - 20) and ball.y <= (pl_right.y + 120):
            # Es wird ueberprueft ob der Ball auf der gleichen x Hoehe ist wie der rechte Spieler.
            if ball.x > 1140 and ball.x <= 1146:
                ball.x = 1140
                ball.velx = ball.velx * -1
        if ball.x >= 1150 and ball.x <= 1290:
            if pl_right.counter == 0:
                if ball.y >= (pl_right.y - 20) and  ball.y <= (pl_right.y - 20 + 6):
                    ball.y = (pl_right.y - 20)
                    ball.vely = ball.vely * -1
                    pl_right.counter += 500
                if ball.y >= (pl_right.y + 100 + 20) and ball.y < (pl_right.y + 100 + 20):
                    ball.y = (pl_right.y + 100 + 20)
                    ball.vely = ball.vely * -1
                    pl_right.counter += 500
