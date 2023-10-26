import socket

#lets create client socket object

clientsocket=socket.socket()

# assign same host and port number as of server
host="127.0.0.1"
port=12334
print("Waiting for Connection")
# we need to setup a connection
try:
    clientsocket.connect((host, port))
except socket.error as e:
    print(str(e))

# printing welcome to server message
Response = clientsocket.recv(1024)
print(Response.decode('utf-8'))
# we need the client to keep running as server is running
while True:
    # lets provide input option so the can send back data to the server
    Input=input("Enter Something ")
    clientsocket.send(str.encode(Input))
    response=clientsocket.recv(2048)
    print(response.decode('utf-8'))

clientsocket.close()