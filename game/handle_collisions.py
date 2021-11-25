from time import sleep


class Handle_Collision:

    def __init__(self):
        pass

    def _collide(self, player, walls, middle):
        self.player = player
        self.walls = walls
        self.middle = middle
        
        if self.player.collides_with_list(self.walls) or self.player.collides_with_list(self.middle):
            if self.player.velocity == (0,1):
                self.player.velocity = (0,-2)
                sleep(.5)
                self.player.velocity = (0,0)
            elif self.player.velocity == (0,-1):
                self.player.velocity = (0,2)
                sleep(.5)
                self.player.velocity = (0,0)
            elif self.player.velocity == (1,0):
                self.player.velocity = (-2,0)
                sleep(.5)
                self.player.velocity = (0,0)
            elif self.player.velocity == (-1,0):
                self.player.velocity = (2,0)
                sleep(.5)
                self.player.velocity = (0,0)