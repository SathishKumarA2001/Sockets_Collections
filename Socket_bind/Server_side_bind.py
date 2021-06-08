import socket
from typing import Tuple

bind_socket = socket.socket()
#Bind the Ip Address and Port
bind_socket.bind(("localhost",3074))
bind_socket.listen()
print("Listening...")

while True:
    client , addr = bind_socket.accept()
    while True:
        recv = client.recv(1024)
        print("Auth from client : ",recv.decode())
        client.sendall("I get you moron take my auth".encode())
        break
    break
client.close()