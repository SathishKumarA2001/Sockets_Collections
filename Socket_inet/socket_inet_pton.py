import socket

#converts 32 bit IPv4 string to 32 binary packed format

ipv4 = "127.0.0.1"
ipv6 = "2401:4900:4835:a69:a853:466b:9cbd:49fa"

bin_v4 = socket.inet_pton(socket.AF_INET,ipv4)
bin_v6 = socket.inet_pton(socket.AF_INET6,ipv6)
print("IPv4 : ",bin_v4)
print("IPv6 : ",bin_v6)


