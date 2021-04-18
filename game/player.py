
from engine_2d.vector2D import Vector2D
from engine_2d.physics import Physics
from engine_2d.shape2D import Shape2D
from models.load_models import get_player_l, get_player_r
from game.limb import Limb

class Player():

    def __init__(self, position:Vector2D):
        self.__body = get_player_l()
        self.__arm = Limb(position+Vector2D([0, 50]), 40, 40, 1)
        self.__player_physics = Physics(position)

        self.__health = 100
        self.__in_air = False
    

    def move_right(self, speed):
        pass


    def move_left(self, speed):
        pass


    def jump(self)-> bool:
        if not self.__in_air:
            pass


    def move_sword(self, direction:Vector2D, speed:float):
        pass


    def check_sword_colision(self, target:Shape2D)-> Vector2D or False:
        pass


    def get_damage(self, value:float)-> bool:
        self.__health += value
        if self.__health < 0:
            self.__health = 0
            return False
        return True

    def calculate(self, deltatime):
        pass
