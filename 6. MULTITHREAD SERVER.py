import socket
from _thread import *
serversocket=socket.socket()

host="127.0.0.1"
port=12334

#thread count for number of threads running
ThreadCount = 0

# lets bind the host and port to the socket server we created
# if it binds successfully it starts waiting for the client

try:
    serversocket.bind((host, port))
except socket.error as e:
    print(str(e))
print("Waiting for connection")
serversocket.listen(5)

# we need to create a function which handles requests from diff client using threads
def client_thread(connection): # we have to receive a connection object
    connection.send(str.encode("Welcome to the server"))
    while True:
        data = connection.recv(2048)
        reply="hello I am server"+data.decode("utf-8") #also sending the same data received
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True: #we need to run this server all time until we stop
    client,address=serversocket.accept()
    print("Connected to "+address[0]+str(address[1]))
    start_new_thread(client_thread,(client,)) #func name and parameters in circular brackets
    ThreadCount+=1
    print("Thread Number: ",ThreadCount)
serversocket.close()


