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
    spawn_block_interval = 0.4

    timers = []
    defeault_timers = []

    def __init__(self):
        self.create_window()
        self.create_player()

    # Main loop of the program.
    def run(self):
        frames_per_second = 60

        # create and start timers
        self.initialise_timers()

        # main loop of the game
        running = True
        while running:
            self.clock.tick(frames_per_second)
            self.screen.fill(self.background_colour)
            
            # handle sprite movement
            self.move_sprites()

            # draw all sprites on screen
            self.draw_sprites()

            # update timers and reset once finished
            self.update_timers()
            
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

    # Create a block and add it to the 'blocks' list.
    def spawn_block(self):
        block_x = self.screen.get_width()*(random.randint(0,2)/3)
        self.blocks.append(Block(self, block_x, -self.height))

    # Get the screen of the game.
    def get_screen(self):
        return self.screen
    
    # Update the timers and remove if finished.
    def update_timers(self):
        for timer in self.timers:
            if not timer.is_alive():
                self.timers.remove(timer)
                self.initialise_timers()

    # Create timers with the recurring functions.
    def initialise_timers(self):
        timer1 = Timer(self.spawn_block_interval, self.spawn_block) # spawn block timer
        if timer1 not in self.timers:
            self.timers.append(timer1)
        for timer in self.timers:
            timer.start()
            