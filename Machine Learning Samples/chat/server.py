import socket

port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket object

CHUNK = 65535

# ip where the server will listen on when message comes

hostname = '127.0.0.1' #localhost

s.bind((hostname, port))

print(f"Server is live on {s.getsockname()}")
# print(f"server is live on {s.getsockname()}")

while True:
    data, clientAdd = s.recvfrom(CHUNK)
    message =data.decode('ascii')
    print(f"Chatter says: {message}")
    message_send = input("Reply: ")
    data = message_send.encode('ascii')
    s.sendto(data, clientAdd)