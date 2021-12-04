"""This class just contols the player, to check if they go off of the screen, and put them back on the other side. 
This class is used for the creation of sprites"""



import arcade
from game import constants

class Player(arcade.Sprite):
    
    def update(self):
        
        self.center_x += self.change_x
        self.center_y += self.change_y
    #check for out of bounds
        if self.left < -2:
            self.right = constants.SCREEN_WIDTH + 2
        
        if self.right > constants.SCREEN_WIDTH + 2:
            self.left = -2