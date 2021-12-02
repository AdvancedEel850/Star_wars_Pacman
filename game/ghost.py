import arcade
from game import constants

class Ghost(arcade.Sprite):

    def update(self):
        
        self.center_x += self.change_x
        self.center_y += self.change_y
    #check for out of bounds
        if self.left < -2:
            self.right = constants.SCREEN_WIDTH + 2
        
        if self.right > constants.SCREEN_WIDTH + 2:
            self.left = -2