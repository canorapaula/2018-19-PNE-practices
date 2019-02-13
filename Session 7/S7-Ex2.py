# Programming a chat for sending many messages to a server

import socket

IP = "212.128.253.66"
PORT = 8083
while True:
    # Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    s.connect((IP, PORT))
    # By asking for a message the server won't crash
    message = input('Please insert a message to send to the server:')
    s.send(str.encode(message))

    # Data from the server
    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:\n")
    print(msg)

    s.close()
