from Sprite import *

class Player(Sprite):

    def __init__(self, game, x=0, y=0, colour = (0, 240, 0)):
        super().__init__(game, x, y, colour)
        # higher width, lower size (screen_height/width is size)
        self.width = 16
        
    # Handle player movement based on input.
    def move(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.x = self.screen.get_width()*(0.175)
                if event.key == pygame.K_s:
                    self.x = self.screen.get_width()*(0.5)
                if event.key == pygame.K_d:
                    self.x = self.screen.get_width()*(0.825)

    # Draw the player on the screen.
    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (self.x, self.y), self.screen.get_height()/self.width)
