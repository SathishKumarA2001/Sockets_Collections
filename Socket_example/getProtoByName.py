import socket

protocol_1 = "TCP"
protocol_2 =  "UDP"
protocol_3 = "ICMP"

TCP = socket.getprotobyname(protocol_1)
UDP = socket.getprotobyname(protocol_2)
ICMP = socket.getprotobyname(protocol_3)

print("The protocol By name TCP:{} UDP:{} ICMP:{}".format(TCP,UDP,ICMP))