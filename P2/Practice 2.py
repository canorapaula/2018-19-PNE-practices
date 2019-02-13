# Practice 2
import socket

class Seq:
    """A class for representing sequences."""
    def __init__(self, strbases):
        print('New sequence created.')

        self.strbases = strbases


IP = "212.128.253.65"
PORT = 8089
while True:
    # Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    s.connect((IP, PORT))

    message = input('Please insert a sequence to send to the server:')
    s.send(str.encode(message))

    # Data from the server
    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:\n")
    print(msg)

    s.close()
