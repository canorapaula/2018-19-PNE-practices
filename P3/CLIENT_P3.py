import socket

# SERVER IP, PORT
IP = "212.128.253.65"
PORT = 8089

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))


while True:
    # The client is blocking the server....  NOT A GOOD DESIGN!!!
    msg = """ATGC
    len
    countA
    percA"""

# Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()
