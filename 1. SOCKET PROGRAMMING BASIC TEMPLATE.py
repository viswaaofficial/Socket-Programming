import socket
import sys #system module
try:
    #reference variable
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    #if socket is not created properly
    print("Failed to create a socket")
    print("Reason : "+str(err))
    sys.exit()
print("Socket Created")

# Now we have to reach to the server process so we ahve to provide target host and port number
target_host=input("Enter the target host name to connect ")
target_port=input("Enter the target port number ")

try:
    sock.connect((target_host,int(target_port))) #Parameter is in the form of a tuple
    print("Socket Connected to : "+target_host+" "+target_port)
except socket.error as err:
    print("Failed to Connect to : "+target_host+" "+target_port)
    print("Reason : "+str(err))
    sys.exit()