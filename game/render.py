from game import constants

class Render:

    def __init__(self, screen):

        _arcade = screen

    def _start_render(self):
        # Clear the screen and start drawing
        _arcade.start_render()

        # Draw a blue circle
        _arcade.draw_circle_filled(
            constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.RADIUS, _arcade.color.YELLOW)

        # Finish drawing
        _arcade.finish_render()