import socket
#lets create socket object
client_sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#DGRAM represents connectionless protocol
msg="Hello UDP Server"
client_sock.sendto(msg.encode("utf-8"),("127.0.0.1",12345))
data,addr = client_sock.recvfrom(4096)
print("server says")
print(str(data))
client_sock.close()