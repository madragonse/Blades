from communication.client import Client
from communication.package import Package
from communication.parser import from_bytes_list
from communication.parser import LOCollector
import time

client = Client(server_port= 5001, server_ip= '169.254.189.31')
package = Package()
tcpLO = LOCollector()
udpLO = LOCollector()

while True:
    #print('SEND')
    package.hit_mark([27,72], 11, 21)
    client.append_udp_send(package.get_bytes())
    package.hit_mark([27,72], 11, 21)
    client.append_tcp_send(package.get_bytes())
    package.hit_mark([27,72], 11, 21)
    client.append_tcp_send(package.get_bytes())
    recived = client.get_tcp_recive()
    a = tcpLO.from_bytes_list(recived)
    if a != []:
        print('TCP health: '+str(a[0]['value']))
    recived = client.get_udp_recive()
    a = udpLO.from_bytes_list(recived)
    if a != []:
        print('UDP health: '+str(a[0]['value']))


    package.hit_mark([27,72], 11, 21)
    client.append_tcp_send(package.get_bytes())
    #time.sleep(2)
    
    package.player_health(2, 99)
    client.append_tcp_send(package.get_bytes())
    #time.sleep(2)
    
    package.player_position(2, [1,2], 0)
    client.append_tcp_send(package.get_bytes())
    #time.sleep(2)
    
    package.sword_position(1, [5, 4], 300)
    client.append_udp_send(package.get_bytes())
    #time.sleep(2)
    
    
