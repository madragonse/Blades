
from typing import List
import socket
import threading
import time 

from communication.package import Package
from communication.playerInstance import Player


class Server():

    def __init__(self, server_port, server_ip=None):
        self.__server_socket_tcp = None
        self.__server_socket_udp = None
        self.__players = []

        if server_ip == None:
            self.__server_ip = socket.gethostbyname(socket.gethostbyname)
        else:
            self.__server_ip = server_ip
        self.__server_port = server_port

        self.__server_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_socket_tcp.bind(server_ip, server_port)

    def __add_player(conn:socket.socket, addr:socket._RetAddress):
        pass

    def listen_for_players(self):
        self.__server_socket_tcp.listen()

        is_looking = True
        while is_looking:
            print('Listening for player...')
            conn, addr = self.__server_socket_tcp.accept()
            self.add_player(conn, addr)
            while True:
                response = input('Look for another player? [y/n]')
                if response == 'y':
                    break
                elif response == 'n':
                    is_looking = False
                    break
                else:
                    print('Wrong input: \"{}\"'.format(response))




    

    def exchange(packages:List)-> List:
        pass 