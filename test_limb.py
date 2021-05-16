from engine_2d.line2D import Line2D
from engine_2d.physics import Physics
from engine_2d.vector2D import Vector2D
from engine_2d.matrixOp import Matrix_op
from engine_2d.shape2D import Shape2D
from engine_2d.collision2D import Collision
import turtle
import keyboard
import time

SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600



def render(pen:turtle.Turtle, line):
    pen.penup()
    pen.goto(line[0][0], line[0][1])
    pen.pendown()
    pen.width(2)
    for i in range(1, line.__len__()):
        pen.goto(line[i][0], line[i][1])
    pen.penup()

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

wn = turtle.Screen()
wn.setup(width = SCREEN_WIDTH + 20, height = SCREEN_HEIGHT + 20)
wn.title("Collision detection test")
wn.bgcolor("black")
wn.tracer(0)

collision_tool = Collision()
l2 = Line2D([[-40, -40], [40,40]])
s2 = Shape2D()
s2.addLine(l2)

from models.load_models import get_player_l, get_player_r
from models.player_model import player_model

from game.limb import Limb

arm = Limb(Vector2D([0, 0]), 100, 100,-1)
while True:
    # Clear the screen  
    pen.clear()
    time.sleep(0.02)

    if keyboard.is_pressed('up'):
        arm.set_end_position(arm.end + Vector2D([0, 6]))
    if keyboard.is_pressed('down'):
        arm.set_end_position(arm.end + Vector2D([0, -6]))
    if keyboard.is_pressed('left'):
        arm.set_end_position(arm.end + Vector2D([-6, 0]))
    if keyboard.is_pressed('right'):
        arm.set_end_position(arm.end + Vector2D([6, 0]))

    if keyboard.is_pressed('w'):
        arm.set_position(arm.position + Vector2D([0, 4]))
    if keyboard.is_pressed('s'):
        arm.set_position(arm.position + Vector2D([0, -4]))
    if keyboard.is_pressed('a'):
        arm.set_position(arm.position + Vector2D([-4, 0]))
        #arm = Limb(arm.position, 100, 100, -1, arm.end)
    if keyboard.is_pressed('d'):
        arm.set_position(arm.position + Vector2D([4, 0]))
        #arm = Limb(arm.position, 100, 100, 1, arm.end)

    arm.calculate()

    pen.color("White")
    linesToDraw = arm.get_sections()
    for line in linesToDraw:
        render(pen, line)  


    wn.update()

# s1 = get_player_r()
# while True:
#     # Clear the screen  
#     pen.clear()
#     #time.sleep(1)
#     s1.set_acceleration([0,0])
#     if keyboard.is_pressed('w'):
#         s1.add_acceleration(Vector2D([0, 1]))
#     if keyboard.is_pressed('s'):
#         s1.add_acceleration(Vector2D([0, -1]))
#     if keyboard.is_pressed('a'):
#         s1.add_acceleration(Vector2D([-1,0]))
#     if keyboard.is_pressed('d'):
#         s1.add_acceleration(Vector2D([1,0]))

#     if keyboard.is_pressed('q'):
#         s1.rotate(0.1)
#     if keyboard.is_pressed('e'):
#         s1.rotate(-0.1) 
    
#     s1.calculate(0.015)
#     res = collision_tool.shapesCollision(s1, s2)
#     if  (res == False): 
#         pen.color("White")
#     else:
#         pen.color("Blue")

#     linesToDraw = s1.getPoints()
#     for line in linesToDraw:
#         render(pen, line) 
#     linesToDraw = s2.getPoints()
#     for line in linesToDraw:
#         render(pen, line) 


#     wn.update()




