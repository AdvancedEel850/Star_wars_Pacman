# Imports
import arcade
from pyglet import window
from game import constants
from game.atat import ATAT
from game.ai import Aritficial
from game.lives import Lives
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
        self.handle_collisions = Handle_Collision()
        self.all_sprites = arcade.SpriteList()
        self.map = arcade.SpriteList()
        self.ghost = arcade.SpriteList()
        self.walls = arcade.SpriteList()
        self.middle = arcade.SpriteList()
        self.dots = arcade.SpriteList()
        self.lives = arcade.SpriteList()
        self._atat = ATAT()
        self._ai = Aritficial()
        self._lives = Lives()
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
        self.mid.left = 220
        self.mid.bottom = 355
        self.middle.append(self.mid)

        self.ghost = self._atat.setup(self.ghost)

        self.dot = arcade.Sprite("Images/blaster.png")
        self.dot.center_x = 430
        self.dot.center_y = 190
        self.dots.append(self.dot)

        self.lives = self._lives._setup()


    def on_draw(self):
        # Clear the screen and start drawing
        arcade.start_render()
 
        self.map.draw()
        self.dots.draw()
        self.all_sprites.draw()
        self.ghost.draw()
        self.lives.draw()


    def on_update(self, delta_time: float):
        
        if len(self.all_sprites) == 0 and len(self.lives) >= 0:
            self.player = Player("Images/Luke.png")
            self.player.center_y = 185
            self.player.center_x = 300
            self.all_sprites.append(self.player)
        self.all_sprites.update()
   
        self.ghost.update()
        self.dots.update()
        self._ai._ai(self.walls, self.ghost)

        self.handle_collisions._collide(self.player, self.walls, self.middle, self.dots, self.ghost, self.lives)
        self._ai.check_collision()

    def on_key_press(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        W/A/S/D: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed"""

        
        if symbol == arcade.key.ESCAPE:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused
            self._ai._ai(self.walls, self.ghost)
            
        if symbol == arcade.key.W or symbol == arcade.key.UP:
            self.player.velocity = (0,1)
            self._ai._ai(self.walls, self.ghost)
            
        if symbol == arcade.key.S or symbol == arcade.key.DOWN:
            self.player.velocity = (0,-1)
            self._ai._ai(self.walls, self.ghost)
            
        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.velocity = (-1, 0)
            self._ai._ai(self.walls, self.ghost)
            
        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.velocity = (1,0)
            self._ai._ai(self.walls, self.ghost)
            

def main():
    window = My_Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.WINDOW_TITLE)
    window._setup()
    arcade.run()

if __name__ == '__main__':
    main()