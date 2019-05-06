import http.server
import socketserver
import termcolor

PORT = 8081


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        pathlist = self.path.split('?')
        print('pathlist: ', pathlist[0])

        if pathlist[0] == '/':
            f = open("form1.html", 'r')
            contents = f.read()

        elif pathlist[0] == '/myserver':
            resource = pathlist[1]
            print('resource: ', resource)
            params = resource.split('&')
            par_msg = params[0].split('=')
            msg = par_msg[1]

            contents = """<!DOCTYPE html>
                                         <html lang="en" dir="ltr">
                                           <head>
                                             <meta charset="utf-8">
                                             <title>CALCULATIONS</title>
                                           </head>
                                           <body style="background-color: ligthyellow;">
                                             <h1>Calculations</h1>
                                             <p>Sequence: {}
                                             <br>Length off
                                             <br>Operation OPERR</p>
                                             <a href="/">Home Link</a>
                                           </body>
                                         </html>
                                 """.format(msg)

            for x in msg:

                if x == 'A' or 'C' or 'G' or 'T':
                    par_leng = params[1].split('=')
                    leng = par_leng[1]
                    par_base = params[2].split('=')
                    base = par_base[1]
                    par_oper = params[3].split('=')
                    oper = par_oper[1]
                    print(leng, base, oper)
                    if leng == 'on':
                        length_sequence = len(msg)
                        contents = contents.replace('Length off', 'Length: {}'.format(length_sequence))
                    elif oper == 'count':
                        A_number = 0
                        C_number = 0
                        T_number = 0
                        G_number = 0
                        for x in msg:
                            if x == 'A':
                                A_number += 1
                            elif x == 'C':
                                C_number += 1
                            elif x == 'T':
                                T_number += 1
                            elif x == 'G':
                                G_number += 1
                        if base == 'A':
                            contents = contents.replace('OPERR', 'Count of A: {}'.format(A_number))
                        elif base == 'C':
                            print(C_number)
                        elif base == 'T':
                            print(T_number)
                        elif base == 'G':
                            print(G_number)

                    elif oper == 'perc':
                        contents = contents.replace('OPERR', 'Percentage:')
                        A_number = 0
                        C_number = 0
                        T_number = 0
                        G_number = 0
                        for x in msg:
                            if x == 'A':
                                A_number += 1
                            elif x == 'C':
                                C_number += 1
                            elif x == 'T':
                                T_number += 1
                            elif x == 'G':
                                G_number += 1
                        if len(msg) > 0:
                            per_A = round(100.0 * A_number / len(msg), 1)
                            per_C = round(100.0 * C_number / len(msg), 1)
                            per_T = round(100.0 * T_number / len(msg), 1)
                            per_G = round(100.0 * G_number / len(msg), 1)

                        else:
                            per_A = 0
                            per_C = 0
                            per_G = 0
                            per_T = 0

                        if base == 'A':
                            print(per_A)
                        elif base == 'C':
                            print(per_C)
                        elif base == 'T':
                            print(per_C)
                        elif base == 'G':
                            print(per_G)



                else:
                    contents = """<!DOCTYPE html>
                            <html lang="en" dir="ltr">
                              <head>
                                <meta charset="utf-8">
                                <title>Error server</title>
                              </head>
                              <body style="background-color: tomato;">
                                <h1>ERROR SERVER</h1>
                                <p>Sorry, the sequence you inserted is wrong. 
                                Try to insert a sequence with the letters A, T, G or C.</p>
                                <a href="/">Home Link</a>
                              </body>
                            </html>
                    """

        else:
            f = open("error.html", 'r')
            contents = f.read()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
