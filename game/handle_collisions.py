"""This class controls player collision with the walls. It uses inheritance to get all of the collision boundries that the player
might run into."""


from time import sleep

import arcade
from game.atat import ATAT

class Handle_Collision:

    def __init__(self):
        pass

    def _collide(self, player, walls, middle, dots, ghost, lives):
        self.player = player
        self.walls = walls
        self.middle = middle
        self.dots = dots
        self.ghost = ghost
        self.lives = lives
        self._atat = ATAT()
        
        if self.player.collides_with_list(self.walls) or self.player.collides_with_list(self.middle):
            if self.player.velocity == (0,2):
                self.player.center_y -= 5
                self.player.velocity = (0,0)
            elif self.player.velocity == (0,-2):
                self.player.center_y += 5
                self.player.velocity = (0,0)
            elif self.player.velocity == (2,0):
                self.player.center_x -=5
                self.player.velocity = (0,0)
            elif self.player.velocity == (-2,0):
                self.player.center_x +=5
                self.player.velocity = (0,0)

        count = len(self.dots)
        for i in range(0, count):
            self.dot = self.dots[i]
            if self.player.collides_with_sprite(self.dot):
                self.dot.remove_from_sprite_lists()
                self.dots.update()
                break

        if self.player.collides_with_list(self.ghost):
            self.player.remove_from_sprite_lists()
            self._atat._reset(self.ghost)
            sleep(1)
            if len(self.lives) == 0:
                arcade.finish_render()
            elif len(self.lives) != 0:
                self.lives[-1].remove_from_sprite_lists()

            
                

        