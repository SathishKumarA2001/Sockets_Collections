import socket

getfqdn = socket.getfqdn() #It gives you the Local python machine interpreter name as "Local"...
print("The Host name of Local python machine interpreter name is : ",getfqdn)

Name = "Example.org"
getfqdn = socket.getfqdn(Name)
print("The Host Name of Example is  : ",getfqdn) #It gives you the Top Level Domain (TLD) .org of given domain
