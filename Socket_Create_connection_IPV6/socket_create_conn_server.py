import socket

socket.setdefaulttimeout(20)
timeout = socket.getdefaulttimeout()
print("The connection will be closed after within {}".format(timeout))
conn = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
conn.bind(('::1',35491))
conn.listen()
print('listening..')

while True:
    connect,addr = conn.accept()
    data = connect.recv(1024)
    print(data.decode())
    connect.sendall('Get my auth!'.encode())
