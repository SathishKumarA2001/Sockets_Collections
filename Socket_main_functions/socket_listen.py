import socket
import datetime
import random

che_quotes = [("Better to die rather than lying on another man's feet"),
                ("The world will be deaf until you dump"),
                ("If you get angry on seeing an unfair situation, then only you are my comrade"),
                ("we are realists so that we dream of impossibilities")]

Ip = "localhost"
port = 3954

conn = socket.socket()
conn.bind((Ip,port))
conn.listen()
print("Listening...")

while True:
    user,addr = conn.accept()
    rand = random.randint(0,4)
    msg = che_quotes[rand]
    user.send(msg.encode())
    time = datetime.datetime.now()
    print("The msg has been sent : {} at : {}".format(msg,time))
    user.close()
    break
conn.close()