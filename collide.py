import player
import ball

pl_left = player.player(x=20, y=300, vel=6, color=(0, 255, 0))
pl_right = player.player(x=1160, y=300, vel=6, color=(0, 0, 255))
ball = ball.ball()

def colllide():
    # Es wird ueberprueft ob der __linke__ Spieler beruehrt wird, wenn ja wird der Ball abgestossen.
    if ball.velx < 0:
        # Es wird überprueft ob der Ball auf der gleichen y-Hoehe ist wie der linke Spieler.
        if ball.y >= (pl_left.y - 10) and ball.y <= (pl_left.y + 110):
            # Es wird überprueft ob der Ball auf der gleichen x-Hoehe ist wie der linke Spieler.
            if ball.x <= 60 and ball.x >= 54:
                ball.x = 60
                ball.velx = ball.velx * -1
        if ball.x >= 10 and ball.x <= 50:
            if pl_left.counter == 0:
                if ball.y >= (pl_left.y - 20) and  ball.y <= (pl_left.y - 20 + 6):
                    ball.y = (pl_left.y - 20)
                    ball.vely = ball.vely * -1
                    pl_left.counter += 60
                if ball.y >= (pl_left.y + 100 + 20 - 6) and ball.y < (pl_left.y + 100 + 20):
                    ball.y = (pl_left.y + 100 + 20)
                    ball.vely = ball.vely * -1
                    pl_left.counter += 60
    # Es wird ueberprueft ob der __rechte__ Spieler beruehrt wird, wenn ja wird der Ball abgestossen.
    elif ball.velx > 0:
        # Es wird ueberprueft ob der Ball auf der gleichen y-Hoehe ist wie der rechte Spieler.
        if ball.y >= (pl_right.y - 10) and ball.y <= (pl_right.y + 110):
            # Es wird ueberprueft ob der Ball auf der gleichen x-Hoehe ist wie der rechte Spieler.
            if ball.x > 1140 and ball.x <= 1146:
                ball.x = 1140
                ball.velx = ball.velx * -1
        if ball.x >= 1150 and ball.x <= 1290:
            if pl_right.counter == 0:
                if ball.y >= (pl_right.y - 20) and  ball.y <= (pl_right.y - 20 + 6):
                    ball.y = (pl_right.y - 20)
                    ball.vely = ball.vely * -1
                    pl_right.counter += 60
                if ball.y >= (pl_right.y + 100 + 20 - 6) and ball.y < (pl_right.y + 100 + 20):
                    ball.y = (pl_right.y + 100 + 20)
                    ball.vely = ball.vely * -1
                    pl_right.counter += 60
