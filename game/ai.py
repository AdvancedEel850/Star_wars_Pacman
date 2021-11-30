from game.atat import ATAT
import random

from time import sleep

class Aritficial(ATAT):

    def __init__(self) -> None:
        super().__init__()

    def _ai(self, walls, ghost):
        
        self.walls = walls
        self.ghost = ghost

        for i in range(0,len(self.ghost)):
            if self.ghost[i].velocity == (0,0):
                self.ghost[i].velocity = (random.randint(-1,1), 0)
    
    def check_collision(self):
        
        for i in range(len(self.ghost)):
            if self.ghost[i].collides_with_list(self.walls):
                if self.ghost[i].velocity == (0,1):
                    self.ghost[i].velocity = (0,-2)
                    sleep(.5)
                    self.ghost[i].velocity = (0,0)
                elif self.ghost[i].velocity == (0,-1):
                    self.ghost[i].velocity = (0,2)
                    sleep(.5)
                    self.ghost[i].velocity = (0,0)
                elif self.ghost[i].velocity == (1,0):
                    self.ghost[i].velocity = (-2,0)
                    sleep(.5)
                    self.ghost[i].velocity = (0,0)
                elif self.ghost[i].velocity == (-1,0):
                    self.ghost[i].velocity = (2,0)
                    sleep(.5)
                    self.ghost[i].velocity = (0,0)