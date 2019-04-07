# Creating a server for the html files with forms, using form1.html and form2.html

import http.server
import socketserver
import termcolor

PORT = 8000

# Objects inherit properties from BaseHTTPRequestHandler


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # -- printing the request line
        termcolor.cprint(self.requestline, 'green')

        f = open("form2.html", 'r')
        contents = f.read()

        # Generate response message with html server
        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body response message
        self.wfile.write(str.encode(contents))

        print()
        termcolor.cprint('Text received', 'cyan')
        mes_dict = self.requestline.split('msg=')
        mes_dict_1 = mes_dict[1].split('&')
        mes_dict_2 = mes_dict_1[0].split('+')
        print(mes_dict_2[0])

        termcolor.cprint('Text received FINISHED', 'cyan')


# -- Main Program
# The "" with nothing in them means use the local IP adress
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server is stopped.")
