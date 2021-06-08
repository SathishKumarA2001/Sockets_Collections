import socket

c_socket = socket.socket()
c_socket.connect(("localhost",3074))
c_socket.send("You moron send me a auth".encode())

while True:
    recv = c_socket.recv(1024)
    print("I got from server : ",recv.decode())
    break
c_socket.close()