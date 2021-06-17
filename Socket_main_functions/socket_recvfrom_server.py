from os import scandir
import socket
##Recvfrom function from server side

def code(msg):
    if msg == "code1":
        return "commit code 1"
    else:
        return "wrong code"

conn = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
conn.bind(("localhost",3094))
print("Listening...")
 
while True:
    reply = conn.recvfrom(1024)
    result = code(reply[0].decode())
    print(reply[0].decode(),":",result)
    conn.sendto(result.encode(),reply[1])
    break
conn.close()