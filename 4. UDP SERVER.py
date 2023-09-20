import socket
#lets create socket object
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #DGRAM represents connectionless protocol
sock.bind(("127.0.0.1",12345))

while True:
    #recv returns data aswell as address
    #in tcp after the connection is established the address information does not change
    #in udp as it is a connectionless protocol we have to receive the address as we have to send the data back
    data,addr=sock.recvfrom(4096) #in udp mesage size should be equal to the packet size
    #printing data we received from client
    print(str(data))
    msg = "Hello, I am UDP Server" #message should be in bytes
    #logic is same we use sendto instead of send
    sock.sendto(msg.encode("utf-8"), addr)

