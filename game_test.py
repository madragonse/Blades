from math import trunc
from game.arena import Game
from engine_2d.vector2D import Vector2D
import keyboard

if __name__ == "__main__":
    print('Do you want to host a game [y/n]?')
    while True:
        if keyboard.is_pressed('y'):
            game = Game(Vector2D([-100, 0]), Vector2D([100, 0]))
            break
        if keyboard.is_pressed('n'):
            print('Insert server IP address:port: ', end='')
            server_addr_s = '169.254.189.31:5004'#input()
            server_addr = server_addr_s.split(':')
            print(server_addr)
            game = Game(Vector2D([-100, 0]), Vector2D([100, 0]), server_address=server_addr[0], server_port=int(server_addr[1]))
            break
    
    game.game_loop()
    print('Game have ended!')