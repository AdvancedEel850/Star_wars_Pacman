# Imports
import arcade
from pyglet import window
from game import constants

class My_Game(arcade.Window):

    def __init__(self, width, height, title):

            super().__init__(width,height,title)

            self._width = width
            self._height = height
            self._title = title

    def _setup(self):
        pass

    def on_draw(self):
        pass

    def on_update(self, delta_time: float):
        pass

def main():
    window = My_Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.WINDOW_TITLE)
    window._setup
    arcade.run()

if __name__ == '__main__':
    main()