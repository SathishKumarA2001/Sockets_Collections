import socket

Addr = ("93.184.216.34",43)
info = socket.getnameinfo(Addr,socket.NI_NOFQDN)
print(info)

Addr = ("93.184.216.34",443)
info = socket.getnameinfo(Addr,socket.NI_NUMERICHOST)
print(info)

Addr = ("93.184.216.34",43)
info = socket.getnameinfo(Addr,socket.NI_NUMERICSERV)
print(info)

Addr = ("93.184.216.34",80)
info = socket.getnameinfo(Addr,socket.NI_NAMEREQD)
print(info)



