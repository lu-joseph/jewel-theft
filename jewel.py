from math import *
from tkinter import *

class Jewel:
    def __init__(self, x, y, big):
        self.x = x
        self.y = y
        self.big = big
        self.screen_jewel = 0
        self.picked_up = False

    def check_collision(self, player, screen):
        distance = sqrt((self.x-player.x)**2 + (self.y-player.y)**2)
        if distance <= 40:
            if self.big:
                if player.got_key:
                    screen.delete(self.screen_jewel)
                    if not self.picked_up:
                        player.score += 1000
                        self.picked_up = True
                    player.got_jewel = True
            else:
                screen.delete(self.screen_jewel)
                if not self.picked_up:
                    player.score += 250
                    self.picked_up = True
