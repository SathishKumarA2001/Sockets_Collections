import socket

socket.setdefaulttimeout(10) #connection will be closed within the defaultTimeOut
timeout = socket.getdefaulttimeout()
print("The connection will be closed after within {}".format(timeout))
conn = socket.create_connection(('localhost',35491))
data = 'Hey let me in!'
conn.sendall(data.encode())

while True:
    data = conn.recv(1024)
    print(data.decode())


