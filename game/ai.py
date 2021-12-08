"""This file controls the main movement for the ghost. It will control the ghost movement to move around the walls This file uses inheritance
 and polymorphism to move the ghost using both the _ai and _check_collision. This class inherits from the ATAT class."""


from game.atat import ATAT
import random

from time import sleep

class Aritficial(ATAT):

    def __init__(self) -> None:
        super().__init__()

    def _ai(self, walls, ghost, player):
        
        self.walls = walls
        self.ghost = ghost
        self.player = player

        for i in range(0,len(self.ghost)):
            self.atat = self.ghost[i]
            if self.atat.velocity == (0,0):
                self.atat.velocity = (random.randint(-1,1), 0)
            
            n = random.randint(1,1000)
            if n > 850 and self.atat.center_x == 300:
                self.atat.velocity = (0,1)
        
        for x in range(0, len(self.ghost)):
            self.atat = self.ghost[x]
            if self.atat.center_x == self.player.center_x and self.atat.center_y > self.player.center_y:
                self.atat.velocity = (0,-1)
            elif self.atat.center_x == self.player.center_x and self.atat.center_y < self.player.center_y:
                self.atat.velocity = (0,1)
            elif self.atat.center_y == self.player.center_y and self.atat.center_x > self.player.center_x:
                self.atat.velocity = (1,0)
            elif self.atat.center_y == self.player.center_y and self.atat.center_x < self.player.center_x:
                self.atat.velocity = (-1,0)

    def check_collision(self):
        
        for i in range(0,len(self.ghost)):
            self.atat = self.ghost[i]
            if self.atat.collides_with_list(self.walls):
                if self.atat.center_y == 410:    
                    if self.atat.velocity == (0,1):
                        self.atat.velocity = (0,0)
                    elif self.atat.velocity == (0,-1):
                        self.atat.velocity = (0,0)
                    elif self.atat.velocity == (1,0):
                        self.atat.velocity = (-1,0)
                    elif self.atat.velocity == (-1,0):
                        self.atat.velocity = (1,0)
                else:
                    if self.atat.velocity == (0,1):
                        self.atat.center_y -= 5
                        self.atat.velocity = (random.randint(-1,1),random.randint(-1,1))
                        for i in range(100):
                            if self.atat.velocity == (0,0) or self.atat.velocity == (1,1) or self.atat.velocity == (0,1) or self.atat.velocity == (1,-1) or self.atat.velocity == (-1,1) or self.atat.velocity == (-1,-1):
                                self.atat.velocity = (random.randint(-1,1),random.randint(-1,1))
                            else:
                                break
                    elif self.atat.velocity == (0,-1):
                        self.atat.center_y += 5
                        self.atat.velocity = (random.randint(-1,1),random.randint(-1,1))
                        for i in range(100):
                            if self.atat.velocity == (0,0) or self.atat.velocity == (1,1) or self.atat.velocity == (0,-1) or self.atat.velocity == (1,-1) or self.atat.velocity == (-1,1) or self.atat.velocity == (-1,-1):
                                self.atat.velocity = (random.randint(-1,1),random.randint(-1,1))
                            else:
                                break
                    elif self.atat.velocity == (1,0):
                        self.atat.center_x -= 5
                        self.atat.velocity = (random.randint(-1,1),random.randint(-1,1))
                        for i in range(100):
                            if self.atat.velocity == (0,0) or self.atat.velocity == (1,1) or self.atat.velocity == (1,0) or self.atat.velocity == (1,-1) or self.atat.velocity == (-1,1) or self.atat.velocity == (-1,-1):
                                self.atat.velocity = (random.randint(-1,1),random.randint(-1,1))
                            else:
                                break
                    elif self.atat.velocity == (-1,0):
                        self.atat.center_x += 5
                        self.atat.velocity = (random.randint(-1,1),random.randint(-1,1))
                        for i in range(100):
                            if self.atat.velocity == (0,0) or self.atat.velocity == (1,1) or self.atat.velocity == (-1,0) or self.atat.velocity == (1,-1) or self.atat.velocity == (-1,1) or self.atat.velocity == (-1,-1):
                                self.atat.velocity = (random.randint(-1,1),random.randint(-1,1))
                            else:
                                break