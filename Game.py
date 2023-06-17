import pygame
from Player import *
from Block import *

class Game:
    __background_colour = (0, 0, 0)
    (__width, __height) = (470, 650)

    def __init__(self):
        self.create_window()
        self.create_player()

    def run(self):
        # main loop of the game
        running = True
        while running:
            self.__clock.tick(60)
            self.__screen.fill(self.__background_colour)
            
            # MAKE THIS A FUNCTION
            # handle player movement
            self.__player.move()
            # handle block movement
            ### for block in self.__blocks:
            ###     block.move()

            # MAKE THIS A FUNCTION
            # handle display
            self.__player.draw()
            ### for block in self.__blocks:
            ###     block.draw()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def create_window(self):
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption('Arcade game')
        self.__screen.fill(self.__background_colour)
        pygame.display.flip()
        self.__clock = pygame.time.Clock()

    def create_player(self):
        self.__player = Player(self.__screen, self.__width*0.50, self.__screen.get_height()*0.9)
