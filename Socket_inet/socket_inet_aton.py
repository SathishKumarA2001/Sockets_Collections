import socket
#converts an 32 bit IP string to packet 32 bit binary format 

ipv4 = "192.178.91.2"
inet = socket.inet_aton(ipv4)
print(inet)