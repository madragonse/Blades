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

# l1 = Line2D([[-10,-15], [10*6,15*6]]) 
l2 = Line2D([[-40, -40], [40,40]])
# l3 = Line2D([[-40, -40], [40,40], [40,900]])
# print(l3)

# s1 = Shape2D([10, 100])
s2 = Shape2D([0, 0])

# s1.addLine(l3)
s2.addLine(l2)


# from models.player_model import player_model

# player_left_origin = player_model['origin']
# #player_left_origin[0] *= -1
# player_left_origin[1] *= -1
# player_left = Shape2D([0, 0])

# for line in player_model['model']:
#     for i in range(0, len(line)):
#         #line[i][0] *= -1
#         line[i][1] *= -1


#     if len(line) == 2:
#         for p in range(0, len(line)):
#             line[p][0] = line[p][0] - player_left_origin[0]
#             line[p][1] = line[p][1] - player_left_origin[1]
#         player_left.addLine(Line2D(line))
#     else:
#         const_line = []
#         const_line.append([line[0][0] - player_left_origin[0], line[0][1] - player_left_origin[1]])
#         for i in range(1, len(line)):
#             const_line.append([const_line[i-1][0] + line[i][0], const_line[i-1][1] + line[i][1]])
#         const_line.append(const_line[0])
#         player_left.addLine(Line2D(const_line))
from models.load_models import get_player_l, get_player_r
from models.player_model import player_model



print(get_player_l())
s1 = get_player_r()
while True:
    # Clear the screen  
    pen.clear()
    #time.sleep(1)
    s1.set_acceleration([0,0])
    if keyboard.is_pressed('w'):
        s1.add_acceleration(Vector2D([0, 1]))
    if keyboard.is_pressed('s'):
        s1.add_acceleration(Vector2D([0, -1]))
    if keyboard.is_pressed('a'):
        s1.add_acceleration(Vector2D([-1,0]))
    if keyboard.is_pressed('d'):
        s1.add_acceleration(Vector2D([1,0]))

    if keyboard.is_pressed('q'):
        s1.rotate(0.1)
    if keyboard.is_pressed('e'):
        s1.rotate(-0.1) 
    
    s1.calculate(0.015)
    res = collision_tool.shapesCollision(s1, s2)
    if  (res == False): 
        pen.color("White")
    else:
        pen.color("Blue")

    linesToDraw = s1.getPoints()
    for line in linesToDraw:
        render(pen, line) 
    linesToDraw = s2.getPoints()
    for line in linesToDraw:
        render(pen, line) 


    wn.update()




