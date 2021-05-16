from typing import List
from engine_2d.vector2D import Vector2D
from game.player import Player
from communication.server import Server
from communication.client import Client
from communication.package import Package
from communication.parser import LOCollector



import turtle
import keyboard
import time

SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600


class Game:
    def __init__(self, controlled_position:Vector2D, oponent_position:Vector2D, server_port=5004, server_address:str = None):
        self.controlled = Player(controlled_position)
        self.opponent = Player(oponent_position, 0)

        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        self.__pen = pen

        wn = turtle.Screen()
        wn.setup(width = SCREEN_WIDTH + 20, height = SCREEN_HEIGHT + 20)
        wn.title("Collision detection test")
        wn.bgcolor("black")
        wn.tracer(0)
        self.__window = wn

        self.__package = Package()
        self.__tcpLO = LOCollector()
        self.__udpLO = LOCollector()

        if server_address == None:
            self.__comm = Server(server_port)
            self.__comm.listen_for_player()
        else:
            self.__comm = Client(server_address, server_port)

        
    def __render(self, pen, line):
        pen.penup()
        pen.goto(line[0][0], line[0][1])
        pen.pendown()
        pen.width(2)
        for i in range(1, line.__len__()):
            pen.goto(line[i][0], line[i][1])
        pen.penup()


    def __draw(self):
        shatpe_to_draw = self.opponent.get_shapes()
        for shape in shatpe_to_draw:
            linesToDraw = shape.getLines()
            for line in linesToDraw:
                self.__render(self.__pen, line) 
        shatpe_to_draw = self.controlled.get_shapes()
        for shape in shatpe_to_draw:
            linesToDraw = shape.getLines()
            for line in linesToDraw:
                self.__render(self.__pen, line) 
        self.__window.update()


    def __mirror_point(self, point:List)-> List:
        ret = []
        ret.extend(point)
        ret[0] = ret[0]*-1
        return ret


    def __mirror_angle(self, angle:int)-> int:
        return


    
    def __send_data(self):
        self.__package.player_position(1, self.__mirror_point(self.controlled.get_position_to_send()), 0)
        self.__comm.append_udp_send(self.__package.get_bytes())
        self.__package.sword_position(1, self.__mirror_point(), )
        self.__comm.append_udp_send(self.__package.get_bytes())

    
    def __recive_data_and_execute(self):
        recived = self.__udpLO.from_bytes_list(self.__comm.get_udp_recive())
        if recived != []:
            for p in recived:
                if p['type'] == 'playerPosition':
                    self.opponent.set_position(Vector2D(p['position']))



    def game_loop(self):
        while True:
            self.__pen.clear()
            time.sleep(0.02)
            # if keyboard.is_pressed('up'):
            #     self.controlled.move(Vector2D([0, 5]))
            # if keyboard.is_pressed('down'):
            #     self.controlled.move(Vector2D([0, -5]))
            if keyboard.is_pressed('left'):
                self.controlled.move(Vector2D([-5, 0]))
            if keyboard.is_pressed('right'):
                self.controlled.move(Vector2D([5, 0]))

            if keyboard.is_pressed('w'):
                self.controlled.move_sword(Vector2D([0, 7]))
            if keyboard.is_pressed('s'):
                self.controlled.move_sword(Vector2D([0, -7]))
            if keyboard.is_pressed('a'):
                self.controlled.move_sword(Vector2D([-7, 0]))
            if keyboard.is_pressed('d'):
                self.controlled.move_sword(Vector2D([7, 0]))
            if keyboard.is_pressed('q'):
                self.controlled.rotate_sword(10)
            if keyboard.is_pressed('e'):
                self.controlled.rotate_sword(-10)

            self.__send_data()

            self.__recive_data_and_execute() 

            self.__draw()

