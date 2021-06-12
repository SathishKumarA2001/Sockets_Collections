import socket
 ## Get port Number of the internet service protocol using service name...

serviceList = ["daytime","ftp","gopher","http","https","imap","pop3","ssh","smtp"]

UnderLying_proto = "tcp"
UnderLying_proto_2 = "udp"

for service in serviceList:
    port = socket.getservbyname(service,UnderLying_proto)
    print("The service port : {} of service Protocol: {}".format(port,service))