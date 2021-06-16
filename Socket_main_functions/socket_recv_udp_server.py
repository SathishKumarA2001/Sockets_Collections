import socket
##Recv function using UDP server

ip = "127.0.0.1"
port = 3094

sckt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sckt.bind((ip,port))
info = "Data from server..."
print("listening...")

while True:
    client_conn = sckt.recvfrom(1024)
    msg = client_conn[0]
    addr = client_conn[1]
    print(client_conn)
    sckt.sendto(info.encode(),addr)
    

