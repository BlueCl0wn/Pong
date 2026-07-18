import pygame
import instances

class var():
    def __init__(self):
        self.run = 1
        self.pausecounter = 0
        self.sizex = 1200
        self.sizey = 675
        self.pause = -1
        self.score_screen = 0  # 0 = no score screen, 1 = show score screen
