import socket
#Converts 32 bit binary format to human readale ipv4 string format 

packed = b"\xc0\xaa\x08\x03"
ipv4 = socket.inet_ntop(socket.AF_INET,packed)
print(ipv4)