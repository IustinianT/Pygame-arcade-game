from Sprite import *

class Block(Sprite):

    def __init__(self, game, x=0, y=0, colour=(240, 0, 0)):
        super().__init__(game, x, y, colour)
        self.width = self.screen.get_width()/3
        self.height = self.screen.get_height()/10
        self.speed = 5

    # Draw the block, given its position.
    def draw(self):
        pygame.draw.rect(self.screen, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

    # Move the block downwards at a steady pace.
    def move(self):
        self.y += self.speed

    # Respawn the block slightly above the window visibility.
    def respawn(self):
        self.y = -self.height

    def is_out_of_bounds(self):
        if self.y >= self.screen.get_height():
            return True
        return False
