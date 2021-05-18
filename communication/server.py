
from typing import List
import socket, ssl
import threading
import time 
from threading import Thread, Semaphore

from communication.package import Package
from communication.player import Player



class Server():


    def __init__(self, server_port, server_ip=None, udp_port= 5006, client_udp_port = 5005):
        self.__client_udp_port = client_udp_port

        self.__server_socket_tcp = None
        self.__server_socket_udp = None
        #self.__players = []#mul
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

        if server_ip == None:
            self.__server_ip = '0.0.0.0'#socket.gethostbyname(socket.gethostname())
        else:
            self.__server_ip = server_ip



        self.__server_port = server_port
        self.__server_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


        self.__server_socket_tcp.bind((self.__server_ip, self.__server_port))
        self.__server_socket_udp.bind((self.__server_ip, udp_port))

        # self.hostname = 'www.test.org'
        # self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        # self.context.load_cert_chain(certfile='cert_V2.pem')#, keyfile='key_V2.pem')

    def __add_player(self, conn:socket.socket, addr):
        if self.__opponent != None:
            raise Exception("Player alredy connected!")
        self.__opponent = Player(conn, addr, 1, [100, 0], 0, [0, 0], 0, 100, 'ready')


    def get_tcp_recive(self) -> List:
        with self.__lock_rec_tcp:
            ret = []
            ret.extend(self.__recive_tcp_data)
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
            #print('RECIVING TCP')
            data = self.__opponent.conn.recv(2048)
            if not data:
                time.sleep(0.01)
                continue
            with self.__lock_rec_tcp:
                self.__recive_tcp_data.append(data)


    def __send_tcp(self):
        while True:
            if len(self.__send_tcp_data) > 0:
                with self.__lock_sen_tcp:
                    for data in self.__send_tcp_data: 
                        #print("SENDING TCP")
                        self.__opponent.conn.send(data)
                    self.__send_tcp_data = []
            time.sleep(0.01)


    def __recive_udp(self):
        while True:
            data = self.__server_socket_udp.recv(2048)
            #print('RECIVING UDP')
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
                        #print("SENDING UDP")
                        self.__server_socket_udp.sendto(data, (self.__opponent.addr[0], self.__client_udp_port))
                    self.__send_udp_data = []
            time.sleep(0.01)
            

    def listen_for_player(self):
        self.__server_socket_tcp.listen()
        print('Listening for player on address {}...'.format(self.__server_ip+':'+str(self.__server_port)))
        #self.__server_socket_tcp = self.context.wrap_socket(self.__server_socket_tcp, server_side=False, server_hostname=None)
        conn, addr = self.__server_socket_tcp.accept()
        self.__add_player(conn, addr)
        print('Player added')
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
        
    

    # def listen_for_players(self):#mul
    #     self.__server_socket_tcp.listen()

    #     is_looking = True
    #     while is_looking:
    #         print('Listening for player...')
    #         conn, addr = self.__server_socket_tcp.accept()
    #         self.add_player(conn, addr)
    #         while True:
    #             response = input('Look for another player? [y/n]')
    #             if response == 'y':
    #                 break
    #             elif response == 'n':
    #                 is_looking = False
    #                 break
    #             else:
    #                 print('Wrong input: \"{}\"'.format(response))





    def exchange(packages:List)-> List:
        pass 