import player
import ball

pl_left = player.player(x=20, y=300, vel=6, color=(0, 255, 0))
pl_right = player.player(x=1160, y=300, vel=6, color=(0, 0, 255))
ball = ball.ball()

def colllide():
    # Es wird überprüft ob der __linke__ Spieler berührt wird, wenn ja wird der Ball abgestoßen.
    if ball.velx < 0:
        # Es wird überprüft ob der Ball auf der gleichen y-Höhe ist wie der linke Spieler.
        if ball.y >= (pl_left.y - 10) and ball.y <= (pl_left.y + 110):
            # Es wird überprüft ob der Bal auf der gleichen x-Höhe ist wie der linke Spieler.
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
    # Es wird überprüft ob der __rechte__ Spieler berührt wird, wenn ja wird der Ball abgestoßen.
    elif ball.velx > 0:
        # Es wird überprüft ob der Ball auf der gleichen y-Höhe ist wie der rechte Spieler.
        if ball.y >= (pl_right.y - 10) and ball.y <= (pl_right.y + 110):
            # Es wird überprüft ob der Ball auf der gleichen x-Höhe ist wie der rechte Spieler.
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
