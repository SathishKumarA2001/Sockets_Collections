import socket
###Recvfrom function from client side

conn = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server = ("localhost",3094)
print("connected...")

conn.sendto("code1".encode(),server)
reply = conn.recvfrom(1024)
print(reply[0].decode())
conn.close()