import socket

Bit32Int = 40333232
Bit16Int = 300

Con32_ntohl = socket.ntohl(Bit32Int)
Con32_htnl = socket.htonl(Con32_ntohl)

print("Bit32Int : {} convert to network byte to host : {}".format(Bit32Int ,Con32_ntohl))
print("Bit32Int : {} convert to host byte to network : {}".format(Con32_ntohl,Con32_htnl))

Con16_ntohs = socket.ntohs(Bit16Int)
Con16_htons = socket.htons(Con16_ntohs)

print("Bit16Int : {} convert to network byte to host : {}".format(Bit16Int ,Con16_ntohs))
print("Bit16Int : {} convert to host byte to network : {}".format(Con16_ntohs,Con16_htons))