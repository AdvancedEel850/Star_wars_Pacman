import arcade

class ATAT():
    
    def __init__(self):
        self.ghost = arcade.SpriteList()
        

    def _start_atat():
        pass

    def _on_update():
        pass

    def _ai():
        pass

    def _setup(self, ghost):
        
        self.ghost = ghost

        if len(self.ghost) < 4:
            for i in range(len(self.ghost), 4):
                self.atat = arcade.Sprite("Images/ATAT.png")
                self.atat.center_y = 410
                self.atat.center_x = self._x_list[i]
                self.ghost.append(self.atat)