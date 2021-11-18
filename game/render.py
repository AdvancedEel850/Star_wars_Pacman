from game import constants

class Render:

    def __init__(self, screen):

        self._arcade = screen
        self.all_sprites = self._arcade.SpriteList()
        self.map = self._arcade.SpriteList()
        self.ghost = self._arcade.SpriteList()
        self.height = 10
        self._setup()

    def _start_render(self):
        # Clear the screen and start drawing
        self._arcade.start_render()
        
        self._draw()

        # Finish drawing
        self._arcade.finish_render()
    
    def _draw(self):
        
        self._arcade.SpriteList.draw(self.map)
        self._arcade.SpriteList.draw(self.ghost)
        self._arcade.SpriteList.draw(self.all_sprites)

    def _setup(self):

        self.player = self._arcade.Sprite("Images/Luke.png")
        self.player.center_y = 185
        self.player.center_x = 300
        self.all_sprites.append(self.player)

        self.background = self._arcade.Sprite("Images/map.png")
        self.background.center_y = constants.SCREEN_HEIGHT/2
        self.background.center_x = constants.SCREEN_WIDTH/2
        self.map.append(self.background)

        self.atat = self._arcade.Sprite("Images/ATAT.png")
        self.atat.center_y = 410
        self.atat.center_x = 340
        self.ghost.append(self.atat)