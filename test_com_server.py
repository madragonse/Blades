from communication.server import Server
from communication.package import Package
import time

server = Server(server_port= 5001)
server.listen_for_player()

package = Package()

while True:
    #time.sleep(3)
    recived = server.get_tcp_recive()
    print('TCP: '+str(recived))
    recived = server.get_udp_recive()
    print('UDP: '+str(recived))
    package.player_health(2, 99)
    server.append_tcp_send(package.get_bytes())
    server.append_udp_send(package.get_bytes())
