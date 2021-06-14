import socket
import struct

#converts 32 bit binary format to ipv4 string format

num =  182436141
bit = struct.pack('!I',num)
ipv4 = socket.inet_ntoa(bit)
print(ipv4)