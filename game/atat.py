import arcade

class ATAT():
    
    def __init__(self) -> None:

        self.ghost = arcade.SpriteList()
        self._x_list = [350, 319, 288, 257]

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
                self.atat = arcade.Sprite("Images/ATAT.png")
                self.atat.center_y = 410
                self.atat.center_x = self._x_list[i]
                self.atat.velocity =(1,0)
                self.ghost.append(self.atat)

        return self.ghost