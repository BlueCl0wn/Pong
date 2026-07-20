from instances import *

def calculate_bounce_angle(player, ball):
    """
    Berechnet den Rückprallwinkel basierend auf der Kollisionsposition auf dem Spieler.
    
    Args:
        player: Der Spieler (pl_left oder pl_right), den der Ball trifft.
        ball: Der Ball, der den Spieler trifft.
    
    Returns:
        tuple: (new_velx, new_vely) - Die neuen Geschwindigkeitskomponenten des Balls.
    """
    # Relative Position des Balls auf dem Spieler (0 = oben, 0.5 = Mitte, 1 = unten)
    relative_pos = (ball.y - player.y) / player.height
    
    # Begrenze die relative Position auf [0, 1], falls der Ball leicht außerhalb trifft
    relative_pos = max(0.0, min(1.0, relative_pos))
    
    # Berechne den Winkel basierend auf der relativen Position
    # Der Winkel wird so berechnet, dass der Ball in Richtung der Mitte des Spielers abgelenkt wird
    # Je weiter oben oder unten der Ball trifft, desto stärker wird er nach oben oder unten abgelenkt
    bounce_angle = (relative_pos - 0.5) * 2.0  # Normalisiert auf [-1, 1]
    
    # Skalierung der vertikalen Geschwindigkeit basierend auf dem Winkel
    # Die maximale vertikale Geschwindigkeit ist die aktuelle Geschwindigkeit des Balls
    max_vely = 9  # Maximale vertikale Geschwindigkeit (aus vel_list)
    new_vely = bounce_angle * max_vely
    
    # Behalte die horizontale Geschwindigkeit bei, aber kehre die Richtung um
    new_velx = -ball.velx
    
    # Normalisiere die Geschwindigkeit, um zu starke Ablenkungen zu vermeiden
    # Die horizontale Geschwindigkeit bleibt dominant, um das Spiel spielbar zu halten
    new_vely = int(new_vely)
    
    return new_velx, new_vely


def colllide():
    # Es wird überprüft, ob der linke Spieler berührt wird, wenn ja wird der Ball abgestoßen.
    if ball.velx < 0:  # Ball bewegt sich nach links
        # Überprüfe, ob der Ball auf der gleichen y-Höhe ist wie der linke Spieler
        if (ball.y >= pl_left.y - ball.radius) and (ball.y <= pl_left.y + pl_left.height + ball.radius):
            # Überprüfe, ob der Ball auf der gleichen x-Höhe ist wie der linke Spieler
            if (ball.x <= pl_left.x + pl_left.width + ball.radius) and (ball.x >= pl_left.x + pl_left.width + ball.radius - 9):
                ball.x = pl_left.x + pl_left.width + ball.radius
                # Berechne den neuen Rückprallwinkel
                new_velx, new_vely = calculate_bounce_angle(pl_left, ball)
                ball.velx = new_velx
                ball.vely = new_vely

        # Kollision mit den oberen/unteren Kanten des Spielers (für Bug-Prävention)
        if ball.x >= pl_left.x and ball.x <= pl_left.x + pl_left.width:
            if pl_left.counter == 0:
                if ball.y >= pl_left.y - ball.radius and ball.y <= pl_left.y - ball.radius + 9:
                    ball.y = pl_left.y - ball.radius
                    ball.vely *= -1
                    pl_left.counter += 500
                if ball.y >= pl_left.y + pl_left.height + ball.radius - 7 and ball.y < pl_left.y + pl_left.height + ball.radius:
                    ball.y = pl_left.y + pl_left.height + ball.radius
                    ball.vely *= -1
                    pl_left.counter += 500

    # Es wird überprüft, ob der rechte Spieler berührt wird, wenn ja wird der Ball abgestoßen.
    elif ball.velx > 0:  # Ball bewegt sich nach rechts
        # Überprüfe, ob der Ball auf der gleichen y-Höhe ist wie der rechte Spieler
        if (ball.y >= pl_right.y - ball.radius) and (ball.y <= pl_right.y + pl_right.height + ball.radius):
            # Überprüfe, ob der Ball auf der gleichen x-Höhe ist wie der rechte Spieler
            if (ball.x > pl_right.x - ball.radius) and (ball.x <= pl_right.x - ball.radius + 9):
                ball.x = pl_right.x - ball.radius
                # Berechne den neuen Rückprallwinkel
                new_velx, new_vely = calculate_bounce_angle(pl_right, ball)
                ball.velx = new_velx
                ball.vely = new_vely

        # Kollision mit den oberen/unteren Kanten des Spielers (für Bug-Prävention)
        if ball.x >= pl_right.x and ball.x <= pl_right.x + pl_right.width:
            if pl_right.counter == 0:
                if ball.y > pl_right.y - ball.radius and ball.y <= pl_right.y - ball.radius + 9:
                    ball.y = pl_right.y - ball.radius
                    ball.vely *= -1
                    pl_right.counter += 500
                if ball.y >= pl_right.y + pl_right.height + ball.radius - 9 and ball.y < pl_right.y + pl_right.height + ball.radius:
                    ball.y = pl_right.y + pl_right.height + ball.radius
                    ball.vely *= -1
                    pl_right.counter += 500
