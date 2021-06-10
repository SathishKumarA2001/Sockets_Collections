import socket

#It gives you a addressinfo of the given host...

#addr_info = socket.getaddrinfo("Example.com",80)
#for i in addr_info:
#    print('\n',i)

addr_info = socket.getaddrinfo("Example.com",80,family=socket.AF_INET,proto=socket.IPPROTO_TCP)
print(addr_info)
addr_info = socket.getaddrinfo("Example.com",80,family=socket.AF_INET6,proto=socket.IPPROTO_TCP)
print(addr_info)