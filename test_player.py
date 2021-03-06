from engine_2d.line2D import Line2D
from engine_2d.physics import Physics
from engine_2d.vector2D import Vector2D
from engine_2d.matrixOp import Matrix_op
from engine_2d.shape2D import Shape2D
from engine_2d.collision2D import Collision
from models.load_models import get_player_l, get_sword
from game.player import Player
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

test_player = Player(Vector2D([0 ,0]))
test_target = Player(Vector2D([50 ,0]), 0)

while True:
    # Clear the screen  
    pen.clear()
    time.sleep(0.02)

    if keyboard.is_pressed('up'):
        test_player.move(Vector2D([0, 5]))
    if keyboard.is_pressed('down'):
        test_player.move(Vector2D([0, -5]))
    if keyboard.is_pressed('left'):
        test_player.move(Vector2D([-5, 0]))
    if keyboard.is_pressed('right'):
        test_player.move(Vector2D([5, 0]))

    if keyboard.is_pressed('w'):
        test_player.move_sword(Vector2D([0, 7]))
    if keyboard.is_pressed('s'):
        test_player.move_sword(Vector2D([0, -7]))
    if keyboard.is_pressed('a'):
        test_player.move_sword(Vector2D([-7, 0]))
    if keyboard.is_pressed('d'):
        test_player.move_sword(Vector2D([7, 0]))
    if keyboard.is_pressed('q'):
        #test_player.set_sword_angle(90)
        test_player.rotate_sword(10)
    if keyboard.is_pressed('e'):
        test_player.rotate_sword(-10)
    
    

    # arm_shape = Shape2D()
    # arm_shape.addLine(Line2D(arm.get_sections()[0]))
    # arm_shape.addLine(Line2D(arm.get_sections()[1]))
    # res = collision_tool.shapesCollision(arm_shape, s2)
    # if(res == False): 
    #     pen.color("White")
    # else:
    #     pen.color("Blue")

    pen.color("White")
    p_shapes = test_player.get_shapes()
    for shapie in p_shapes:
        linesToDraw = shapie.getLines()
        for line in linesToDraw:
            render(pen, line) 
    
    if test_player.check_sword_colision(test_target.get_body()) == False or test_player.check_sword_colision(test_target.get_sword()) != False:
        pen.color("White")
    else:
        pen.color("Red")

    p_shapes = test_target.get_shapes()
    for shapie in p_shapes:
        linesToDraw = shapie.getLines()
        for line in linesToDraw:
            render(pen, line) 


    wn.update()
