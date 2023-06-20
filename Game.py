import pygame
import random
from Player import *
from Block import *
from threading import Timer

class Game:
    background_colour = (0, 0, 0)
    (width, height) = (470, 650)
    blocks = []
    current_block_index = 0

    def __init__(self):
        self.create_window()
        self.create_player()

    def run(self):
        frames_per_second = 60
        spawn_block_interval = 0.5
        timer1 = Timer(spawn_block_interval, self.spawn_block)
        timer1.start()
        # main loop of the game
        running = True
        while running:
            self.clock.tick(frames_per_second)
            self.screen.fill(self.background_colour)
            
            # handle sprite movement
            self.move_sprites()

            # draw all sprites on screen
            self.draw_sprites()

            # spawn a block every x seconds
            if not timer1.is_alive():
                timer1 = Timer(spawn_block_interval, self.spawn_block)
                timer1.start()
            
            # if user presses X quit 'cleanly'
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    # Initialise the pygame window.
    def create_window(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Arcade game')
        self.screen.fill(self.background_colour)
        pygame.display.flip()
        self.clock = pygame.time.Clock()

    # Initialise the player.
    def create_player(self):
        # the position of the player based on screen dimensions
        initial_x = 0.5 
        initial_y = 0.9
        self.player = Player(self, self.screen.get_width()*initial_x, self.screen.get_height()*initial_y)

    # Draw all sprites on the screen.
    def draw_sprites(self):
        self.player.draw()
        for block in self.blocks:
            block.draw()
        pygame.display.update()

    # Move all sprites on the screen.
    def move_sprites(self):
        self.player.move()
        for block in self.blocks:
            block.move()
            if block.is_out_of_bounds():
                self.blocks.remove(block)

    def spawn_block(self):
        block_x = self.screen.get_width()*(random.randint(0,2)/3)
        self.blocks.append(Block(self, block_x, -self.height))

    def get_screen(self):
        return self.screen
    