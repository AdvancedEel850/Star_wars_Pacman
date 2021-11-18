from game import constants

class Render:

    def __init__(self, screen):

        self._arcade = screen
        self.all_sprites = []
        self.height = 10
        self._setup()

    def _start_render(self):
        # Clear the screen and start drawing
        self._arcade.start_render()
        

        # Finish drawing
        self._arcade.finish_render()
    
    def _setup(self):

        self.player = self._arcade.Sprite("Images/Luke.png")
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)