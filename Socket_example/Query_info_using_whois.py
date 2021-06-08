import socket

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #By default AF_INET,SOCK_STREAM
clientSocket.connect(('whois.com',443))
print("Connected...")
clientSocket.sendall("example.com".encode())

while True:
    data = clientSocket.recv(4096)
    data = data.decode().splitlines()
    if len(data) > 0:
        for line in data:
            print(line)
    if data==0:
        print('connection closed..')
        break
    break
#clientSocket.close()
