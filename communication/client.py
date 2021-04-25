
from typing import List
import socket
import threading
import time

from communication.package import Package


class Client():

    def __init__(self, server_ip, server_port):
        self.__server_ip = server_ip
        self.__server_port = server_port

    
    def __connect(self):
        pass


    def exchange(packages:List)-> List:
        pass 