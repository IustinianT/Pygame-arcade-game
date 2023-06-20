import pygame
import random

class Sprite:

    def __init__(self, game, x=0, y=0, colour=(255, 255, 255)):
        self.screen = game.get_screen()
        self.x = x
        self.y = y
        self.colour = colour

    # Draws the sprite.
    def draw(self):
        pass

    def move(self):
        pass
