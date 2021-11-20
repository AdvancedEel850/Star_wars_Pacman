
import arcade


class wall_creation():

    def __init__(self, screen) -> None:
        
        self._arcade = screen
        self._walls = self._arcade.SpriteList()
        self._top_list = [712, 712, 712, 712, 612, 612, 612, 612, 612, 387, 312, 387, 237, 237, 237, 237, 160, 160, 160, 462, 800, 387]
        self._left_list = [57, 165, 356, 484, 57, 165, 228, 356, 484, 165, 228, 420, 57, 165, 356, 484, 57, 228, 357, 228, 0, 0]

    def create_walls(self):

        for i in range(22):
            self.wall = self._arcade.Sprite(f"Images/wall{i + 1}.png")
            self.wall.left = self._left_list[i]
            self.wall.top = self._top_list[i]
            self._walls.append(self.wall)
        
        return self._walls
    