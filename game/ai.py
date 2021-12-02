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
            self.atat = self.ghost[i]
            if self.atat.velocity == (0,0):
                self.atat.velocity = (random.randint(-1,1), 0)
    
    def check_collision(self):
        
        for i in range(0,len(self.ghost)):
            self.atat = self.ghost[i]
            if self.atat.collides_with_list(self.walls):
                if self.atat.velocity == (0,1):
                    self.atat.velocity = (0,0)
                elif self.atat.velocity == (0,-1):
                    self.atat.velocity = (0,0)
                elif self.ghost[i].velocity == (1,0):
                    self.ghost[i].velocity = (-2,0)
                    sleep(.5)
                    self.ghost[i].velocity = (0,0)
                elif self.ghost[i].velocity == (-1,0):
                    self.ghost[i].velocity = (2,0)
                    sleep(.5)
                    self.ghost[i].velocity = (0,0)