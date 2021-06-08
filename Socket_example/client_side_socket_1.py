import socket

socketObject = socket.socket()
socketObject.connect(("example.com",80))
print("Connection Established")

msg = """GET / HTTP/1.1"""
bytes = msg.encode()
socketObject.sendall(bytes)

while(True):
    data = socketObject.recv(1024)
    print(data.decode())
    if (data == b''):
        print("Connection Closed")
        break
socketObject.close()
