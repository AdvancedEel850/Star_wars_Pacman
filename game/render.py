from game import constants
from game.map import Map

class Render:

    def __init__(self, screen):

        self._arcade = screen
        self._map = Map(self._arcade)

    def _start_render(self):
        # Clear the screen and start drawing
        self._arcade.start_render()
        
        self._map._draw()
        
        self._arcade.draw_circle_filled( constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.RADIUS, self._arcade.color.YELLOW)

        # Finish drawing
        self._arcade.finish_render()