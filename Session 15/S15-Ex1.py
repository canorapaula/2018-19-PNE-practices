# Exercise 1, session 15. Creating an echo server that creates a html page with the info.

import http.server
import socketserver
import termcolor

PORT = 8009

# Objects inherit properties from BaseHTTPRequestHandler


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')

        f = open("Ex1-form.html", 'r')
        contents = f.read()

        if self.requestline.startswith("GET / ") or self.requestline.startswith("GET /echo "):
            file = open('Ex1_form.html', 'r')
            contents = file.read()
        else:
            file = open('Ex1-form.html', 'r')
            contents = file.read()

        # Generate response message with html server
        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body response message
        self.wfile.write(str.encode(contents))


# -- Main Program
# The "" with nothing in them means use the local IP adress
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped.")
