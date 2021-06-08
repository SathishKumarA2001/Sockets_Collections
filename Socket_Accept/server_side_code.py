import socket
import datetime

server_socket = socket.socket()
server_socket.bind(("127.0.0.1",3074)) #bind the IP and Port in the server side..
print("listening.....")
server_socket.listen() # Listening for incoming connection from the client side

while True:
    (connection, Address ) = server_socket.accept() #Accept the client requests without any filter and stores the connection and Address in the tuples
    TimeNow = str(datetime.datetime.now()) #Capture the time when the client connect
    connection.sendall(TimeNow.encode()) # Send the time to the client when it was connected
    print('Time: {} Address: {}'.format(TimeNow,Address))
    connection.close() #close the client connection
    print("connection Closed...")
    break
    
server_socket.close() #close the socket connection
