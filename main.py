# Imports
import arcade
from pyglet import window
from game import constants
from game.player import Player
from game.walls import wall_creation
from game.handle_collisions import Handle_Collision
from time import sleep

class My_Game(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width,height,title)

        self._wall = wall_creation(arcade)
        self._width = width
        self._height = height
        self._title = title
        self.handle_collisions = Handle_Collision
        self._x_list = [350, 319, 288, 257]
        self.all_sprites = arcade.SpriteList()
        self.map = arcade.SpriteList()
        self.ghost = arcade.SpriteList()
        self.walls = arcade.SpriteList()
        self.middle = arcade.SpriteList()
        arcade.set_background_color(arcade.color.WHITE)

    def _setup(self):

        self.player = Player("Images/Luke.png")
        self.player.center_y = 185
        self.player.center_x = 300
        self.all_sprites.append(self.player)

        self.background = arcade.Sprite("Images/map.png")
        self.background.center_y = constants.SCREEN_HEIGHT/2
        self.background.center_x = constants.SCREEN_WIDTH/2
        self.map.append(self.background)
        
        self.walls = self._wall.create_walls()

        self.mid = arcade.Sprite("Images/mid.png")
        self.mid.left = 227
        self.mid.down = 379
        self.middle.append(self.mid)

        if len(self.ghost) < 4:
            for i in range(len(self.ghost), 4):
                self.atat = arcade.Sprite("Images/ATAT.png")
                self.atat.center_y = 410
                self.atat.center_x = self._x_list[i]
                self.ghost.append(self.atat)

    def on_draw(self):
        # Clear the screen and start drawing
        arcade.start_render()
 
        self.map.draw()
        self.all_sprites.draw()
        self.ghost.draw()


      
    def on_update(self, delta_time: float):
        
        self.all_sprites.update()

        self.handle_collisions._collide(Handle_Collision,self.player, self.walls, self.middle)

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
            self.player.velocity = (0,1)

        if symbol == arcade.key.S or symbol == arcade.key.DOWN:
            self.player.velocity = (0,-1)

        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.velocity = (-1, 0)

        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.velocity = (1,0)
    

def main():
    window = My_Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.WINDOW_TITLE)
    window._setup()
    arcade.run()

if __name__ == '__main__':
    main()