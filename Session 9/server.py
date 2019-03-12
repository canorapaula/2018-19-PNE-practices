# Creating my first server from scratch

import socket

PORT = 8080
IP = "212.128.253.66"
# Max number of clients sending a request
MAX_OPEN_REQUEST = 5

# Function defined to create an echo server:


def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    print("Message from the client: {}".format(msg))

    # Sending the message back to the client(since we are an echo server)
    cs.send(str.encode(msg))

    cs.close()


# Create a socket for connecting to the clients. The parametres are always the same.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

# Listen to the client's requests
serversocket.listen(MAX_OPEN_REQUEST)

print('Socket ready {}'.format(serversocket))

while True:

    print("waiting for connections at: {}".format(IP, PORT))
    # This blocks the server and waits till a client it's connected, it returns the clients socket and the clients IP:
    (clientsocket, address) = serversocket.accept()

    # -- Process the client's request
    print("Attending client: {}".format(address))

    process_client(clientsocket)
