import socket

client_socket = socket.socket()
Server_IP = "127.0.0.1"
Server_Port = 3074 
print("connected to the server,waiting for the response....")

try:
    client_socket.connect((Server_IP,Server_Port))  #connect to the server wit IP and Port in the tuple
    Response = client_socket.recv(1024)    
    print("Response From the server: {}".format(Response.decode()))

except Exception as ex:
    print("Exception Occured: ",ex)
    client_socket.close() #close the connection if Exception occured

finally:
    client_socket.close() #close the connection Always 