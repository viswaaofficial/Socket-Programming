# sends data to the crient and receives data from the client
import socket

# lets create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# first lets bind server
server_socket.bind(('127.0.0.1', 12345))

# server listens - it takes a backlog parameter
server_socket.listen(5)
# 5 connections are keep waiting if the server is busy and if a sixth socket is trying to connect
# then the sever connection is refused

while True:
    print("Server waiting for connection")
    # accept method initiate a connection with the client and it return a new socket object representing the connection and tuple holding the address of the client
    client_socket, addr = server_socket.accept()
    print("Client connected from ", addr)

    # now lets create another while loop to get the data and send the data to the client
    while True:
        # recv method is used to receive data from the client
        # receive atmost 1024 bytes
        data = client_socket.recv(1024)
        if not data or data.decode('utf-8')=="END":
            break
        print("received from client : %s", data.decode("utf-8"))
        try:
            client_socket.send(bytes("Hey Client", "utf-8"))  # here we have to send in form of bytes not string
        except:
            print("Exited by the user")
    client_socket.close()
server_socket.close()