from time import sleep


class Handle_Collision:

    def __init__(self):
        pass

    def _collide(self, player, walls, middle, dots):
        self.player = player
        self.walls = walls
        self.middle = middle
        self.dots = dots
        
        if self.player.collides_with_list(self.walls) or self.player.collides_with_list(self.middle):
            if self.player.velocity == (0,1):
                self.player.center_y -= 5
                self.player.velocity = (0,0)
            elif self.player.velocity == (0,-1):
                self.player.center_y += 5
                self.player.velocity = (0,0)
            elif self.player.velocity == (1,0):
                self.player.center_x -=5
                self.player.velocity = (0,0)
            elif self.player.velocity == (-1,0):
                self.player.center_x +=5
                self.player.velocity = (0,0)

        count = len(self.dots)
        for i in range(0, count):
            dot = self.dots[i]
            if self.player.collides_with_list(self.dots):
                dot.remove_from_sprite_lists()
        