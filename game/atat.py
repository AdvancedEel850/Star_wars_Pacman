
"""This class is the base class for the ghost or atat's. this is the class that sets them up, and uses polymorphism with the ai class.
This also uses encapsulation for the x list"""


import arcade

from game.ghost import Ghost

class ATAT():
    
    def __init__(self) -> None:

        self.ghost = arcade.SpriteList()
        self._x_list = [350, 319, 288, 260]

    def _start_atat(self):
        pass

    def _on_update(self):
        self._ai()

    def _ai(self, walls, ghost):
        pass

    def check_collision(self):
        pass

    def setup(self, ghost):
        
        self.ghost = ghost

        if len(self.ghost) < 4:
            for i in range(len(self.ghost), 4):
                self.atat = Ghost("Images/ATAT.png")
                self.atat.center_y = 410
                self.atat.center_x = self._x_list[i]
                self.atat.velocity = (0,0)
                self.ghost.append(self.atat)

        return self.ghost

    def _reset(self, ghost):
        self.ghost = ghost
        count = len(self.ghost)
        for i in range(0, count):
            self.atat = self.ghost[i]
            self.atat.center_y = 410
            self.atat.center_x = self._x_list[i]
            self.atat.velocity = (0,0)
            self.ghost.update()