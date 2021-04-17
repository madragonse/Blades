from engine_2d.line2D import Line2D
from engine_2d.physics import Physics
from engine_2d.vector2D import Vector2D
from engine_2d.matrixOp import Matrix_op
from engine_2d.shape2D import Shape2D
from engine_2d.collision2D import Collision
import turtle
import keyboard

SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600



def render(pen:turtle.Turtle, line):
    pen.penup()
    pen.goto(line[0][0], line[0][1])
    pen.pendown()
    pen.width(2)
    pen.goto(line[1][0], line[1][1])
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

l1 = Line2D([[-10,-15], [10*6,15*6]]) 
l2 = Line2D([[-40, -40], [40,40]])

s1 = Shape2D([1, 1])
s2 = Shape2D([0, 0])

s1.addLine(l1)
s2.addLine(l2)


# test = Vector2D([1,1])
# v = [2,1]
# i = 2

# print(test*i)

while True:

    # Clear the screen  
    pen.clear()

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

    linesToDraw = s1.getLinesToDraw()
    for line in linesToDraw:
        render(pen, line) 
    linesToDraw = s2.getLinesToDraw()
    for line in linesToDraw:
        render(pen, line) 


    wn.update()




