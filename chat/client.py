import socket

port = 3000
CHUNK = 65535

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket object

# DHCP assigned by os when blank

hostname = '127.0.0.1'
while True:
    s.connect((hostname,port))
    message = input("Type message: ")
    data = message.encode('ascii')
    s.send(data)
    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f"Ellertone says: {text}")