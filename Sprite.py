import pygame
import random

class Sprite:

    def __init__(self, screen, x=0, y=0, colour=(255, 255, 255)):
        self._screen = screen
        self._x = x
        self._y = y
        self._colour = colour

    # Draws the sprite.
    def draw(self):
        pass

    def move(self):
        pass
