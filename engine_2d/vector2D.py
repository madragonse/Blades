
from math import sqrt
from typing import List

class Vector2D:
    
    def __init__(self, pos:"Vector2D"):
        
        if(isinstance(pos, Vector2D)):
            self.__position = pos.getPosition()
        else:
            self.__position = []
            self.__position.extend(pos)
        
    def move(self, v):
        self.__position[0] += v[0]
        self.__position[1] += v[1]

    def set(self, position):
        self.__position = []
        self.__position.extend(position)

    def getPosition(self):
        ret = []
        ret.extend(self.__position)
        return ret

    def getX(self):
        return self.__position[0]

    def getY(self):
        return self.__position[1]

    def length(self):
        return sqrt(pow(self.__position[0], 2)+pow(self.__position[1], 2))

    def normalise(self):
        return self/self.length()

    def __truediv__(self, divider):
        return Vector2D([self.__position[0]/divider, self.__position[1]/divider])
    
    def __add__(self, component):
        if type(component) == Vector2D:
            return Vector2D([self.__position[0]+component.getX(), self.__position[1]+component.getY()])
        # elif type(component) == list:
        #     return Vector2D([self.__position[0]+component[0], self.__position[1]+component[1]])
        else:
            return Vector2D([self.__position[0]+component, self.__position[1]+component])

    def __sub__(self, subtractor):
        return Vector2D([self.__position[0]-subtractor.getX(), self.__position[1]-subtractor.getY()])

    def __mul__(self, multiplier):
        return Vector2D([self.__position[0]*multiplier, self.__position[1]*multiplier])

    def __str__(self):
        return str(self.__position)

    def mul_v(self, mv):
        return Vector2D([self.__position[0]*mv.getX(), self.__position[1]*mv.getY()])