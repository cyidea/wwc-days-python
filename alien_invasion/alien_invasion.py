import sys

import pygame

from settings import Settings
from ship import Ship

class AlientInvasion:
    """Overall cls to manage game assets and behavior."""

    def __init__(self) -> None:
        """initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """ start the main loop for the game. """
        while True:
            self.__check_events()

            # redraw the screen during each pass through the loop.
            self.__update_screen()
            self.clock.tick(60)

    def __check_events(self):
        """ watch for the keyboard and mouse events. """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
    def __update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlientInvasion()
    ai.run_game()
