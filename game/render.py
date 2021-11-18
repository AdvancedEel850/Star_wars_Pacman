from game import constants
import arcade
from main import My_Game
from game.player import Player
from game.background import Background
from game.atat import ATAT

class Render(My_Game):

    def __init__(self, screen):

        self._arcade = screen
        self.all_sprites = self._arcade.SpriteList()
        self.map = self._arcade.SpriteList()
        self.ghost = self._arcade.SpriteList()
        self._x_list = [350,321,290,259]
        


    def _setup(self):

        self.player = Player("Images/Luke.png")
        self.player.center_y = 185
        self.player.center_x = 300
        self.all_sprites.append(self.player)

        self.background = Background("Images/map.png")
        self.background.center_y = constants.SCREEN_HEIGHT/2
        self.background.center_x = constants.SCREEN_WIDTH/2
        self.map.append(self.background)
        
        if len(self.ghost) < 4:
            for i in range(len(self.ghost), 4):
                self.atat = ATAT("Images/ATAT.png")
                self.atat.center_y = 410
                self.atat.center_x = self._x_list[i]
                self.ghost.append(self.atat)

    def on_draw(self):
        # Clear the screen and start drawing
        arcade.start_render()
 
        self.map.draw()
        self.player.draw()
        self.ghost.draw()


      
    def on_update(self, delta_time: float):
        
        self.all_sprites.update()

    def on_key_press(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        W/A/S/D: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed"""

        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.W or symbol == arcade.key.UP:
            self.player.change_y = 1

        if symbol == arcade.key.A or symbol == arcade.key.DOWN:
            self.player.change_y = -1

        if symbol == arcade.key.S or symbol == arcade.key.LEFT:
            self.player.change_x = -1

        if symbol == arcade.key.d or symbol == arcade.key.RIGHT:
            self.player.change_x = 1
    