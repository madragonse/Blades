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
        self.rotate(0)
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


    def getPoints(self):
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

    
    def getLines(self):
        ret = []
        for line in self.__lines:
            points = line.getPoints()
            last_point = points[0]
            for i in range(1, len(points)):
                section = [self.__matrix_op.multiply_vector(self.__rotation_matrix, last_point), self.__matrix_op.multiply_vector(self.__rotation_matrix, points[i])]
                section[0][0] += self._position.getX()
                section[1][0] += self._position.getX()
                section[0][1] += self._position.getY()
                section[1][1] += self._position.getY()
                ret.append(section)
                last_point = points[i]
        return ret

    
    def __str__(self):
        return str(self.getLines())



    
