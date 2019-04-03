# Exercise 1, session 15. Creating an echo server that creates a html page with the info.

import http.server
import socketserver
import termcolor

PORT = 8080

# Objects inherit properties from BaseHTTPRequestHandler


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')
        print(self.path)
        pathlist = self.path.split('?')
        print(pathlist)
        resource = pathlist[0]
        print(resource)
        if resource == "/":
            file = open('Ex1-form.html', 'r')
            contents = file.read()
        elif resource == "/echo":
            params = pathlist[1]
            user_message = params.split("=")
            message = user_message[1]
            contents = """
            <!DOCTYPE html>
            <html lang="en">
            <head>     
                <meta charset="UTF-8">     
                <title>Echo server</title>     
            </head>     
            <body>     
            <h1>Echo of the received message</h1>     
            <p>{}<p>                                  
            <a href="/">Home Page</a>     
            </body>     
            </html>""".format(message)
        else:
            file = open('Ex1-error.html', 'r')
            contents = file.read()
        # Generate response message with html server
        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body response message
        self.wfile.write(str.encode(contents))


# -- Main Program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped.")
