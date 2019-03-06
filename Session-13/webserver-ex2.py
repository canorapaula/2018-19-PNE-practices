import http.server
import socketserver

PORT = 8000
content = ''

class TestHandler(http.server.BaseHTTPRequestHandler):

    def process_client(cs):

        msg = cs.recv(2048).decode("utf-8")

        if msg.startswith("GET / "):
            file = open('index2.html', 'r')
            content = file.read()
        else:
            file = open('error.html', 'r')
            content = file.read()
        print()
        print("Request message: ", msg)

        status_line = "HTTP/1.1 200 ok\r\n"

        header = "Content-Type: text/html\r\n"
        header += "Content-Length: {}\r\n".format(len(str.encode(content)))

        response_msg = status_line + header + "\r\n" + content

        cs.send(str.encode(response_msg))
        cs.close()


    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("   Cmd:   " + self.command)
        print("   Path:   " + self.path)

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    httpd.serve_forever()
