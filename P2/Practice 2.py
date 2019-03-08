# Practice 2. Send server a sequence, its reverse and its complement

import socket


class Seq:

    """A class for representing sequences."""
    def __init__(self, strbases):
        print('New sequence created.')

        self.strbases = strbases


IP = "212.128.253.70"
PORT = 8089
while True:
    # Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('\nSocket created')
    s.connect((IP, PORT))

    # Asking the user for the sequence
    message = input('Please insert a sequence to send to the server:')
    s.send(str.encode(message))

    # Calculating and sending the reversed sequence
    reversed_seq = message[::-1]
    s.send(str.encode("\nThe reversed sequence is:"))
    s.send(str.encode(reversed_seq))

    # Calculating and sending the complement sequence
    complement = []
    for x in message:
        if x == 'A':
            complement.append('T')
        elif x == 'T':
            complement.append('A')
        elif x == 'C':
            complement.append('G')
        elif x == 'G':
            complement.append('C')

    complement = ''.join(complement)
    s.send(str.encode('\nThe complement is:'))
    s.send(str.encode(complement))

    # Data from the server
    msg = s.recv(2048).decode("utf-8")
    print("\nMessage from the server:")
    print(msg)

    s.close()
