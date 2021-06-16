import socket
###UDP recv funtion from client..

sckt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip = ("127.0.0.1",3094)
print("connected..")
i = 0
while i<5:
    msg = "msg from client"
    sckt.sendto(msg.encode(),ip)
    i=i+1
#sckt.sendto(msg.encode(),ip)
msg = sckt.recv(1024)
print(msg.decode())

    