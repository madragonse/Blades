from communication.server import Server
from communication.package import Package
from communication.parser import from_bytes_list
from communication.parser import LOCollector
import time

server = Server(server_port= 5001)
server.listen_for_player()

package = Package()

tcpLO = LOCollector()
udpLO = LOCollector()

while True:
    recived = server.get_tcp_recive()
    tcp = tcpLO.from_bytes_list(recived)
    #print('TCP: '+str(recived))
    recived = server.get_udp_recive()
    udp = udpLO.from_bytes_list(recived)
    #print('UDP: '+str(recived))
    package.player_health(2, 199)
    server.append_udp_send(package.get_bytes())
    package.player_health(2, 99)
    server.append_tcp_send(package.get_bytes())
    print("Tcp: " + str(tcp))
    print("Udp: " + str(udp))
