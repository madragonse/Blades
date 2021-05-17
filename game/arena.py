from tkinter.constants import TRUE
from typing import List
from engine_2d.vector2D import Vector2D
from game.player import Player
from communication.server import Server
from communication.client import Client
from communication.package import Package
from communication.parser import LOCollector
from models.load_models import get_hearth, get_looser_model, get_winner_model, get_tag_model
from datetime import datetime
from timeit import default_timer as timer

import random
import turtle
import keyboard
import time

SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600
HIT_DAMAGE = 20
SPEED = 0.4

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
        wn.colormode(255)
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

        self.__hit = False
        self.__last_hit = False
        self.__hitted = False
        self.__tag = get_tag_model(0.3)
        self.__tag_e = get_tag_model(0.4)
        self.__tag_e.v = 0

        self.__game_on = {'val':True, 'winner':None}
        self.__hearth = get_hearth()

        
    def __render(self, pen, line):
        pen.penup()
        pen.goto(line[0][0], line[0][1])
        pen.pendown()
        pen.width(2)
        for i in range(1, line.__len__()):
            pen.goto(line[i][0], line[i][1])
        pen.penup()


    def __draw(self):
        # print(self.__last_hit, end=' ')
        # print(self.__hit)
        if self.__last_hit != self.__hit and self.__hit == True:
            self.__last_hit = self.__hit
            self.__pen.color('red')
        else:
            self.__last_hit = self.__hit
            self.__pen.color('white')
        shatpe_to_draw = self.opponent.get_shapes()
        for shape in shatpe_to_draw:
            linesToDraw = shape.getLines()
            for line in linesToDraw:
                self.__render(self.__pen, line) 
        
        if self.__hitted == True:
            self.__hitted = False
            self.__pen.color('red')
        else:
            self.__pen.color((220,255,220))
        shatpe_to_draw = self.controlled.get_shapes()
        for shape in shatpe_to_draw:
            linesToDraw = shape.getLines()
            for line in linesToDraw:
                self.__render(self.__pen, line) 
        
        pos_h = [-200*2, 200*2]
        for i in range(0, int(self.controlled.health/HIT_DAMAGE)):
            pos_h[0] += 70
            self.__hearth.set_position(Vector2D(pos_h))
            linesToDraw = self.__hearth.getLines()
            for line in linesToDraw:
                self.__render(self.__pen, line) 

        if self.__hit:
            self.__pen.color('red')
        else:
            self.__pen.color('yellow')
        linesToDraw = self.__tag.getLines()
        for line in linesToDraw:
            self.__render(self.__pen, line) 

        self.__pen.color('red')
        if self.__tag_e.v > 0:
            self.__tag_e.v -= 1
            linesToDraw = self.__tag_e.getLines()
            for line in linesToDraw:
                self.__render(self.__pen, line) 

        self.__window.update()
        


    def __mirror_point(self, point:List)-> List:
        ret = []
        ret.extend(point)
        ret[0] = ret[0]*-1
        return ret


    def __mirror_angle(self, angle:int)-> int:
        return 360 - angle


    def check_hit(self):
        body = self.controlled.check_sword_colision(self.opponent.get_body())
        sword = self.controlled.check_sword_colision(self.opponent.get_sword())
        if body == False or sword != False:
            if sword == False:
                ret = {'target':'air', 'position':None}
                self.__tag.set_position(Vector2D([3000,0]))
            else:
                ret = {'target':'sword', 'position':sword}
                self.__tag.set_position(Vector2D(sword))
        else:
            ret = {'target':'body', 'position':body}
            self.__tag.set_position(Vector2D(body))
        
        return ret

    
    def __send_data(self):
        self.__package.player_position(1, self.__mirror_point(self.controlled.get_position_to_send()), 0)
        self.__comm.append_udp_send(self.__package.get_bytes())
        
        self.__package.sword_position(1, self.__mirror_point(self.controlled.get_sword_position_to_send()), self.__mirror_angle(self.controlled.get_sword_angle_to_send()))
        self.__comm.append_udp_send(self.__package.get_bytes())

        hit = self.check_hit()
        if hit['target'] == 'sword':
            # self.__package.hit_mark(hit['position'], 0, 0, 'sword')
            # self.__comm.append_udp_send(self.__package.get_bytes())
            self.__hit = False
        elif hit['target'] == 'body':
            self.__package.hit_mark(self.__mirror_point(hit['position']), 0, 0, 'body')
            self.__comm.append_udp_send(self.__package.get_bytes())
            if self.__hit == False:
                self.__hit = True
                self.opponent.set_damage(HIT_DAMAGE)
                self.__package.player_health(1, self.opponent.health)
                self.__comm.append_tcp_send(self.__package.get_bytes())
        else:
            self.__hit = False

    
    def __recive_data_and_execute(self):
        recived = self.__udpLO.from_bytes_list(self.__comm.get_udp_recive())
        recived.extend(self.__tcpLO.from_bytes_list(self.__comm.get_tcp_recive()))
        if recived != []:
            for p in recived:
                if p['type'] == 'playerPosition':
                    self.opponent.set_position(Vector2D(p['position']))
                    
                if p['type'] == 'swordPosition':
                    self.opponent.set_sword_angle(int(p['angle']))
                    self.opponent.set_sword_position(Vector2D(p['position']))
                
                if p['type'] == 'playerHealth':
                    self.__hitted = True
                    self.controlled.health = p['value']
                    print(self.controlled.health)
                    if self.controlled.health == 0:
                        self.__game_on['val'] = False
                        self.__game_on['winner'] = False
                        self.__package.game_status('iLost')
                        self.__comm.append_tcp_send(self.__package.get_bytes())
                
                if p['type'] == 'gameStatus':
                    self.__game_on['val'] = False
                    self.__game_on['winner'] = True
                
                if p['type'] == 'hitMark':
                    if p['target'] == 'body':
                        self.__tag_e.set_position(Vector2D(p['position']))
                        self.__tag_e.v = 50



    def winner(self):
        scull = get_winner_model(3)
        scull.set_position(Vector2D([-200*1.3, 200*1]))
        for i in range(0, 300):
            self.__pen.color((20, random.randint(100, 255), 0))
            #self.__pen.clear()
            
            linesToDraw = scull.getLines()
            for line in linesToDraw:
                self.__render(self.__pen, line) 

            self.__window.update()
            time.sleep(0.05)


    def looser(self):
        scull = get_looser_model(10)
        scull.set_position(Vector2D([-200*1, 200*1]))
        for i in range(0, 300):
            self.__pen.color(random.randint(100, 255), 0, 0)
            #self.__pen.clear()
            
            linesToDraw = scull.getLines()
            for line in linesToDraw:
                self.__render(self.__pen, line) 

            self.__window.update()
            time.sleep(0.05)

            
    



    def game_loop(self):
        start = timer()
        while self.__game_on['val']:
            while timer() - start < 0.01:
                time.sleep(0.0001)
            start = timer()
            self.__pen.clear()
            time.sleep(0.01)

            # if keyboard.is_pressed('up'):
            #     self.controlled.move(Vector2D([0, 5]))
            # if keyboard.is_pressed('down'):
            #     self.controlled.move(Vector2D([0, -5]))
            if keyboard.is_pressed('left'):
                self.controlled.move(Vector2D([-5*SPEED, 0]))
                #self.controlled.move_sword(Vector2D([-5*SPEED, 0]))
            if keyboard.is_pressed('right'):
                self.controlled.move(Vector2D([5*SPEED, 0]))
                #self.controlled.move_sword(Vector2D([5*SPEED, 0]))

            if keyboard.is_pressed('w'):
                self.controlled.move_sword(Vector2D([0, 7*SPEED]))
            if keyboard.is_pressed('s'):
                self.controlled.move_sword(Vector2D([0, -7*SPEED]))
            if keyboard.is_pressed('a'):
                self.controlled.move_sword(Vector2D([-7*SPEED, 0]))
            if keyboard.is_pressed('d'):
                self.controlled.move_sword(Vector2D([7*SPEED, 0]))
            if keyboard.is_pressed('q'):
                self.controlled.rotate_sword(9*SPEED)
            if keyboard.is_pressed('e'):
                self.controlled.rotate_sword(-9*SPEED)

            self.__send_data()

            self.__recive_data_and_execute() 

            self.__draw()
        
        if self.__game_on['winner']:
            print('YOU WIN')
            self.winner()
        else:
            print('YOU LOOST')
            self.looser()

