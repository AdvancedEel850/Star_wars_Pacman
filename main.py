# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
import arcade
from game import constants
from game.render import Render

_arcade = arcade
_render = Render(_arcade)

# Open the window
arcade.open_window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

# Set the background color
arcade.set_background_color(arcade.color.WHITE)

# Display everything
_render._start_render()
arcade.run()