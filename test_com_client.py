from communication.client import Client
from communication.package import Package
import time

client = Client(server_port= 5001, server_ip= '169.254.189.31')
package = Package()
for i in range(0, 100):
    print('SEND')
    package.hit_mark([27,72], 11, 21)
    client.append_udp_send(package.get_bytes())
    time.sleep(1)
    package.hit_mark([27,72], 11, 21)
    client.append_tcp_send(package.get_bytes())
    time.sleep(1)
    package.hit_mark([27,72], 11, 21)
    client.append_tcp_send(package.get_bytes())
    time.sleep(1)
    recived = client.get_tcp_recive()
    print('TCP: '+str(recived))
    recived = client.get_udp_recive()
    print('UDP: '+str(recived))
    # package.hit_mark([27,72], 11, 21)
    # client.append_tcp_send(package.get_bytes())
    # time.sleep(2)
    
    # print('SEND')
    # package.player_health(2, 99)
    # client.append_tcp_send(package.get_bytes())
    # time.sleep(2)
    
    # print('SEND')
    # package.player_position(2, [1,2], 0)
    # client.append_tcp_send(package.get_bytes())
    # time.sleep(2)
    
    # print('SEND')
    # package.sword_position(1, [5, 4], 300)
    # client.append_tcp_send(package.get_bytes())
    # time.sleep(2)
    
    
