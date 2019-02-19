# Server for the 3rd practice. It performs operations on a sequence: total length, finding the number of a base and
# the percentage of a base in the sequence


import socket

PORT = 8089
IP = "212.128.253.66"
# Max number of clients sending a request
MAX_OPEN_REQUEST = 5


def length(s):
    return len(s)
def percentage(s):
    tl = len(s)
    return
# Function defined to create an echo server:


def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    print("Message from the client: {}".format(msg))
    length_msg = print('The length is {}'.format(length(msg)))
    cs.send(str.encode(length_msg))

    # Sending the message back to the client(since we are an echo server
    cs.send(str.encode(msg))

    cs.close()


# Create a socket for connecting to the clients. The parameters are always the same.
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
