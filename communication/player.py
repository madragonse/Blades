


class Player():

    def __init__(self, conn, addr, id, position, angle, sword_position, sword_angle, health, status):
        self.conn = conn
        self.addr = addr
        
        self.id = id
        self.position = position
        self.angle = angle
        self.sword_position = sword_position
        self.sword_angle = sword_angle
        self.health = health
        self.status = status
