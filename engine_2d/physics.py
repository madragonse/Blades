
from .vector2D import Vector2D


class Physics():

    def __init__(self, point:Vector2D):
        self._position = Vector2D(point)
        self.__v = Vector2D([0,0]);
        self.__a = Vector2D([0,0]);
    
    def set_speed(self, nv):
        self.__v = Vector2D(nv)
    
    def set_acceleration(self, na):
        self.__a = Vector2D(na)
    
    def add_speed(self, av:Vector2D):
        self.__v += av

    def add_acceleration(self, aa:Vector2D):
        self.__a += aa

    def get_speed(self):
        return Vector2D(self.__v)

    def get_acceleration(self):
        return Vector2D(self.__a)

    def get_position(self):
        return Vector2D(self._position)
    
    def calculate(self, deltatime):
        new_speed = self.__v + (self.__a * deltatime)
        self._position += (self.__v + new_speed) / 2 * deltatime
        self.__v = new_speed

    def decelarate_by(self, dec):
        self.__a -= self.__a.mul_v(dec)