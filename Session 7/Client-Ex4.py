# Connecting to the server of MY computer

import socket

IP = "212.128.253.65"
PORT = 8080

# Create the socket. Always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

# Connection to the Server (IP, PORT)
s.connect((IP, PORT))

message = input('Please insert a message to send to the server:')
s.send(str.encode(message))

# Receive data from the server
msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER:\n")
print(msg)

s.close()

print('The end')
