import math

from .physics import Physics
from typing import List
from .line2D import Line2D
from .vector2D import Vector2D 
from .matrixOp import Matrix_op

class Shape2D(Physics):

    def __init__(self, position):
        super().__init__(position)
        self.__lines = []
        self.__rotation_matrix = [[1,1],[1,1]]
        self.__rotation_angle = 0
        self.__matrix_op = Matrix_op()


    def addLine(self, line:Line2D):
        self.__lines.append(line)
    

    def rotate(self, angle):
        self.__rotation_angle += angle
        if self.__rotation_angle > 360:
            self.__rotation_angle = self.__rotation_angle % 360
        if self.__rotation_angle < 0:
            self.__rotation_angle += 360
        rad = (self.__rotation_angle / 180) * math.pi
        sin_res = math.sin(rad)
        cos_res = math.cos(rad)
        self.__rotation_matrix = [[cos_res, sin_res], [-sin_res, cos_res]]

    def getLinesToDraw(self):
        ret = []
        
        for line in self.__lines:
            tem = line.getPoints()
            for i in range(0, tem.__len__()):
                tem[i] = self.__matrix_op.multiply_vector(self.__rotation_matrix, tem[i])
                tem[i][0] += self._position.getX()
                tem[i][1] += self._position.getY()
            ret.append(tem)
        return ret
    def move(self, v):
        self._position.move(v)


    
