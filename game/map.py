from arcade.window_commands import start_render
from game import constants

class Map:

    def __init__(self, screen):

        self._arcade = screen

    def _draw(self):

        self._arcade.start_render()

        for i in range(0, constants.SCREEN_WIDTH):
            for n in range(0,constants.SCREEN_HEIGHT):
                 self._arcade.draw_circle_filled(i, n, 15, self._arcade.color.BLUE)

        self._arcade.finish_render()