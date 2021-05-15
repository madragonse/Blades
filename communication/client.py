
from ast import Str
from typing import List
import socket
import threading
import time
from threading import Thread, Semaphore
import asyncio
from communication.package import Package


class Client():

    def __init__(self, server_ip:Str, server_port:int, udp_port = 5005, server_udp_port = 5006):
        self.__server_ip = server_ip
        self.__server_port = server_port
        self.__server_udp_port = server_udp_port

        self.__socket_tcp = None
        self.__socket_udp = None
        self.__opponent = None
        self.__lock_rec_tcp = Semaphore(2)
        self.__lock_sen_tcp = Semaphore(3)
        self.__lock_rec_udp = Semaphore(4)
        self.__lock_sen_udp = Semaphore(5)
        self.__send_tcp_data = []
        self.__send_udp_data = []
        self.__recive_tcp_data = []
        self.__recive_udp_data = []
        self.__listening = False

        self.__socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket_udp.bind((socket.gethostbyname(socket.gethostname()), udp_port))

        self.__connect()


    def get_tcp_recive(self) -> List:
        with self.__lock_rec_tcp:
            ret = self.__recive_tcp_data
            self.__recive_tcp_data = []
            return ret


    def append_tcp_send(self, data:bytes):
        with self.__lock_sen_tcp:
            self.__send_tcp_data.append(data)

    
    def get_udp_recive(self) -> List:
        with self.__lock_rec_udp:
            ret = self.__recive_udp_data
            self.__recive_udp_data = []
            return ret


    def append_udp_send(self, data:bytes):
        with self.__lock_sen_udp:
            self.__send_udp_data.append(data)


    def __recive_tcp(self):
        while True:
            print('RECIVING')
            data = self.__socket_tcp.recv(2048)
            if not data:
                time.sleep(0.001)
                continue
            with self.__lock_rec_tcp:
                self.__recive_tcp_data.append(data)


    def __send_tcp(self):
        while True:
            if len(self.__send_tcp_data) > 0:
                with self.__lock_sen_tcp:
                    for data in self.__send_tcp_data: 
                        print("SENDING TCP")
                        self.__socket_tcp.send(data)
                    self.__send_tcp_data = []
            time.sleep(0.001)

    def __recive_udp(self):
        while True:
            data = self.__socket_udp.recv(2048)
            print('RECIVING UDP')
            if not data:
                time.sleep(0.01)
                continue
            with self.__lock_rec_udp:
                self.__recive_udp_data.append(data)


    def __send_udp(self):
        while True:
            if len(self.__send_udp_data) > 0:
                with self.__lock_sen_udp:
                    for data in self.__send_udp_data: 
                        print("SENDING UDP")
                        self.__socket_udp.sendto(data, (self.__server_ip, self.__server_udp_port))
                    self.__send_udp_data = []
            time.sleep(0.01)


    
    def __connect(self):
        self.__socket_tcp.connect((self.__server_ip, self.__server_port))
        print('Connected to server')
        print('Starting transmission in thread')
        self.__listening = True
        tcp_rec_th = Thread(target = self.__recive_tcp, daemon = True)
        tcp_sen_th = Thread(target = self.__send_tcp, daemon = True)
        udp_rec_th = Thread(target = self.__recive_udp, daemon = True)
        udp_sen_th = Thread(target = self.__send_udp, daemon = True)

        tcp_rec_th.start()
        tcp_sen_th.start()
        udp_rec_th.start()
        udp_sen_th.start()



    def exchange(packages:List)-> List:
        pass 