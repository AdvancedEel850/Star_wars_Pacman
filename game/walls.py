
import arcade


class wall_creation():

    def __init__(self, screen) -> None:
        
        self._arcade = screen
        self._walls = self._arcade.SpriteList()
        self._down_list = [660, 660, 660, 660, 584, 584, 286, 286, 210, 210, 435, 512, 586, 510, 435, 510, 285, 210, 210, 135, 210, 135, 60, 85, 135, 60, 60, 90, 435, 535, 435, 535, 760, 660, 445, 445, 360, 360, 360, 285, 0, 135, 0, 285, 10, 135]
        self._left_list = [57, 164, 354, 483, 57, 483, 164, 419, 164, 356, 164, 188, 225, 290, 419, 354, 225, 290, 57, 100, 483, 484, 57, 164, 225, 289, 354, 420, 0, 590, 480, 0, 0, 291, 324, 225, 232, 365, 241, 0, 0, 15, 5, 480, 590, 546, 547]

    def create_walls(self):

        for i in range(46):
            self.wall = self._arcade.Sprite(f"Images/wall{i + 1}.png")
            self.wall.left = self._left_list[i]
            self.wall.bottom = self._down_list[i]
            self._walls.append(self.wall)
        
        return self._walls
    