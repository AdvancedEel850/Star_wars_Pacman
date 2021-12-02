import arcade

class Lives():

    def __init__(self) -> None:
        
        self.livesn = 3
        self.lives = arcade.SpriteList()
        self._x_list = [20, 40, 60]

    def _setup(self):

        n = self.livesn

        for i in range(0, n):
            self.life = arcade.Sprite("Images/Lukelives.png")
            self.life.center_y = 785
            self.life.center_x = self._x_list[i]
            self.lives.append(self.life)

        return self.lives