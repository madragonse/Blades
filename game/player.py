
from engine_2d.vector2D import Vector2D
from engine_2d.physics import Physics
from engine_2d.shape2D import Shape2D
from engine_2d.line2D import Line2D
from models.load_models import get_player_l, get_player_r, get_sword
from game.limb import Limb
from engine_2d.collision2D import Collision

class Player():

    def __init__(self, position:Vector2D, controlled= 1):
        if controlled == 1:
            self.__body = get_player_l()
        else:
            self.__body = get_player_r()

        self.__sword = get_sword()

        if controlled == 1:
            self.__arm = Limb(position+Vector2D([0, 50]), 80, 80, 1)
        else:
            self.__arm = Limb(position+Vector2D([0, 50]), 80, 80, -1)
        
        self.__player_physics = Physics(position)

        self.__position = position
        self.__sword_position = position
        self.__sword_angle = 0

        self.health = 100
        self.__in_air = False

        self.__collision_tool = Collision()
    

    def set_position(self, position:Vector2D, angle = 0):
        #self.__body.set_position(position)
        self.__position = position

    
    def move(self, s:Vector2D, angle = 0):
        self.__position = self.__position + s


    def set_sword_position(self, position:Vector2D):
        if self.__arm.set_end_position(position) == 0:
            self.__sword_position = position
    

    def move_sword(self, s:Vector2D):
        self.__arm.set_end_position(self.__arm.end + s)


    def move_arm(self, s:Vector2D):
        self.__arm.set_position(self.__arm.position + s)


    def rotate_sword(self, angle):
        self.__sword.rotate(angle)


    def jump(self)-> bool:
        if not self.__in_air:
            pass

    
    def get_body(self):
        return self.__body
    
    def get_sword(self):
        return self.__sword

    
    def check_sword_colision(self, target:Shape2D)-> Vector2D or False:
        res = self.__collision_tool.shapesCollision(target, self.__sword)
        return res


    def get_damage(self, value:float)-> bool:
        self.__health += value
        if self.__health < 0:
            self.__health = 0
            return False
        return True


    def calculate(self):
        self.__body.set_position(self.__position)
        self.__arm.set_position(self.__position)
        self.__arm.calculate()
        self.__sword.set_position(self.__arm.end)
        

    def get_shapes(self):
        self.calculate()
        ret = []
        arm_shape = Shape2D()
        arm_shape.addLine(Line2D(self.__arm.get_sections()[0]))
        arm_shape.addLine(Line2D(self.__arm.get_sections()[1]))
        ret.append(arm_shape)
        ret.append(self.__body)
        ret.append(self.__sword)
        return ret


    def get_position_to_send(self):
        return self.__position.getPosition()