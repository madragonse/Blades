
from turtle import position
from engine_2d.line2D import Line2D
from math import pi, sqrt, sin, cos
from engine_2d.vector2D import Vector2D

from engine_2d.vector2D import Vector2D
from engine_2d.matrixOp import Matrix_op

class Limb():

    def __init__(self, position:Vector2D, length1, length2, dir=-1):
        self.__matrix_op = Matrix_op()

        self.length1 = length1
        self.length2 = length2
        self.position = position
        self.end = (position + (length1 / sqrt(2)))
        self.__dir = dir
        self.__rotation_matrix = None
        self.rotate()
        self.calculate()


    def set_position(self, position:Vector2D):
        self.position = position

    
    def set_end_position(self, position:Vector2D):
        if (position - self.position).length() > (self.length1 + self.length2):
            return 1
        else:
            self.end = position
            return 0


    def rotate(self):
        
        end_relative = self.end - self.position
        sin_val = end_relative.getX()/end_relative.length()
        cos_val = end_relative.getY()/end_relative.length()
        self.__rotation_matrix = [[cos_val, self.__dir*sin_val], [self.__dir*-sin_val, cos_val]]

    
    def calculate(self):
        self.rotate()
        length = self.end - self.position
        length = length.length()


        x = length + (( pow(self.length1, 2) - pow(self.length2, 2) - pow(length, 2) )/( 2*length ))

        y = sqrt(pow(self.length1, 2) - pow(x, 2))

        self.joint = Vector2D([x, y])


    def get_sections(self):
        ret = []

        joint_rel = self.joint - self.position
        joint_rel = self.__matrix_op.multiply_vector(self.__rotation_matrix, joint_rel.getPosition())
        corr_rot =  pi /2
        joint_rel = self.__matrix_op.multiply_vector([[cos(corr_rot), self.__dir*-sin(corr_rot)], [self.__dir*sin(corr_rot), cos(corr_rot)]], joint_rel)
        joint_rel[1] *=self.__dir*-1
        joint = Vector2D(joint_rel)
        joint = joint + self.position

        ret.append([self.position.getPosition(), joint.getPosition()])
        ret.append([joint.getPosition(), self.end.getPosition()])
        return ret

    # def get_points(self):
    #     return [self.position.getPosition(), self.joint.getPosition(), self.end.getPosition()]
