import socket
#Get internet service protocol name using service protocol...

ports = [443,80,21,22]
proto = "tcp"

for port in ports:
    name = socket.getservbyport(port,proto)
    print("The service name {} got by port {}".format(name,port))