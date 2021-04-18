
import json
from typing import List


class Package():


    def __init__(self):
        self.__message:str = None


    def get_bytes(self)-> bytes:
        if self.__message == None:
            raise Exception('No message!')
        return self.__message.encode()


    def __str__(self) -> str:
        return(str(self.__message))


    def player_position(self, player_id:int, position:List, angle:float):
        message_content = {
            'type' : 'playerPosition',
            'playerId' : player_id, 
            'position' : position,
            'angle' : angle
        }
        self.__message = json.dumps(message_content)
        pass


    def sword_position(self, player_id:int, position:List, angle:float):
        message_content = {
            'type' : 'swordPosition',
            'playerId' : player_id, 
            'position' : position,
            'angle' : angle
        }
        self.__message = json.dumps(message_content)
        pass


    def player_health(self, player_id:int, value:float):
        message_content = {
            'type' : 'playerHealth',
            'playerId' : player_id, 
            'value' : value
        }
        self.__message = json.dumps(message_content)


    def hit_mark(self, position:List, angle:float, speed:float):
        message_content = {
            'type' : 'hitMark',
            'position' : position, 
            'angle' : angle, 
            'speed' : speed
        }
        self.__message = json.dumps(message_content)
