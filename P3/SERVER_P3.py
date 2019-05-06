# Server for the 3rd practice. It performs operations on a sequence: total length, finding the number of a base and
# the percentage of a base in the sequence

import socket

PORT = 8083
IP = "212.128.253.66"
# Max number of clients sending a request
MAX_OPEN_REQUEST = 5


def length(s):
    return len(s)


def percentage(s):
    tl = len(s)
    print(tl)
    return


def count(s):
    A_number = 0
    C_number = 0
    T_number = 0
    G_number = 0
    for x in s:
        if x == 'A':
            A_number += 1
        elif x == 'C':
            C_number += 1
        elif x == 'T':
            T_number += 1
        elif x == 'G':
            G_number += 1
    return A_number, T_number, G_number, C_number

# Function defined to create an echo server:
def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    message = msg.split('\n')
    print("Message from the client: {}".format(message))

# Si esta el blank, solo tiene que returnear alive, lo demas que haya escrito el client da igual. Al igual que con una
    # sec que da error, solo envia error y ya esta. Por lo demas la secuencia siempre va a estar en primer  lugar
    # en la lista
    if message[0] == '':
        print('Alive')

    # length_msg = print('The length is {}'.format(length(msg))) I DON'T THINK I NEED THIS, SO JUST LEAVE IT JUST IN CASE YK
    cs.send(str.encode(length))

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


#  messagefromclient.split(\n) --> Asi lo que haces es separar el mensaje en una lista y luego el server lee el primer
#  argumento de la liSTA Y MIRA SI ESTA BIEN LUEGO EL 2 Y SI ES LEN HACE LA LEN SI ES COMPa PUES ESO, Y ASI