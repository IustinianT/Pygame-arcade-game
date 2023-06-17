from Sprite import *

class Player(Sprite):

    def __init__(self, screen, x=0, y=0, colour = (0, 240, 0)):
        Sprite.__init__(self, screen, x, y, colour)
        
    def move(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self._x = self._screen.get_width()*(0.25)
                if event .key == pygame.K_s:
                    self._x = self._screen.get_width()*(0.50)
                if event .key == pygame.K_d:
                    self._x = self._screen.get_width()*(0.75)

    def draw(self):
        pygame.draw.circle(self._screen, self._colour, (self._x, self._y), 20)                
