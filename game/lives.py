
"""This file uses the principle of encapsulation with one of the variables. The x_list variable is private, 
as this is the only file that uses that variable. Other files have the same, but this one is made for this class."""

import arcade

class Lives():

    def __init__(self) -> None:
        
        self.livesn = 3
        self.lives = arcade.SpriteList()
        self.__x_list = [20, 40, 60]

    def _setup(self):

        n = self.livesn

        for i in range(0, n):
            self.life = arcade.Sprite("Images/Lukelives.png")
            self.life.center_y = 785
            self.life.center_x = self.__x_list[i]
            self.lives.append(self.life)

        return self.lives