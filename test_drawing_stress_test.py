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
from models.load_models import get_hearth
from timeit import default_timer as timer

from game.limb import Limb
pos = 0
hearth = get_hearth()
stoper = 0
while True:
    # Clear the screen  
    pen.clear()
    time.sleep(0.02)

    if keyboard.is_pressed('up'):
        pos +=5
    if keyboard.is_pressed('down'):
        pos -=5

    print(timer() - stoper)
    stoper = timer()
    
    
    pos_h = [-200*4 + pos, 0]
    for i in range(0, 200):
        pos_h[0] += 30
        hearth.set_position(Vector2D(pos_h))
        linesToDraw = hearth.getLines()
        for line in linesToDraw:
            render(pen, line)



    wn.update()





