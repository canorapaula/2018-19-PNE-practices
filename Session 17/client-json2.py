# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import termcolor
import json


PORT = 8001
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

print("CONTENT: ")

# -- Print the received data
print()

for data in person:
    termcolor.cprint("Name: ", 'green', end='')
    print(data['Firstname'], data['Lastname'])
    termcolor.cprint("Age: ", 'green', end='')
    print(data['age'])
    phones = data['phoneNumber']
    termcolor.cprint("Phone Numbers: ", 'green', end='')
    print(len(phones))
    for i, num in enumerate(data['phoneNumber']):
        termcolor.cprint(" Phone {}".format(i), 'blue', end='')
        termcolor.cprint("\n\tType: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("\tNumber: ", 'red', end='')
        print(num['number'])
    print()
