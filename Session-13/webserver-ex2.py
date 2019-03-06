import http.server
import socketserver

PORT = 8001


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        request_line = self.requestline
        print("Request line:" + request_line)
        print("   Cmd:   " + self.command)
        print("   Path:   " + self.path)

        if request_line.startswith("GET / "):
            file = open('index2.html', 'r')
            content = file.read()
        else:
            file = open('error.html', 'r')
            content = file.read()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    httpd.serve_forever()
