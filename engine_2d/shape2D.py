import math

from .physics import Physics
from typing import List
from .line2D import Line2D
from .vector2D import Vector2D 
from .matrixOp import Matrix_op

class Shape2D():

    def __init__(self, position:Vector2D = None):
        #super().__init__(position)
        self.__lines = []
        self.__rotation_matrix = [[1,1],[1,1]]
        self.__rotation_angle = 0
        self.rotate(0)
        self.__matrix_op = Matrix_op()
        if position == None:
            self.__position = Vector2D([0, 0])
        else:
            self.__position = position

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


    def move(self, v:List):
        self.__position = self.__position+v

    def set_position(self, position:Vector2D):
        self.__position = position


    def get_position(self):
        return self.__position


    def getPoints(self):
        ret = []
        
        for line in self.__lines:
            tem = line.getPoints()
            for i in range(0, tem.__len__()):
                tem[i] = self.__matrix_op.multiply_vector(self.__rotation_matrix, tem[i])
                tem[i][0] += self.__position.getX()
                tem[i][1] += self.__position.getY()
            ret.append(tem)
        return ret

    
    def getLines(self):
        ret = []
        for line in self.__lines:
            points = line.getPoints()
            last_point = points[0]
            for i in range(1, len(points)):
                section = [self.__matrix_op.multiply_vector(self.__rotation_matrix, last_point), self.__matrix_op.multiply_vector(self.__rotation_matrix, points[i])]
                section[0][0] += self.__position.getX()
                section[1][0] += self.__position.getX()
                section[0][1] += self.__position.getY()
                section[1][1] += self.__position.getY()
                ret.append(section)
                last_point = points[i]
        return ret

    
    def __str__(self):
        return str(self.getLines())



    
