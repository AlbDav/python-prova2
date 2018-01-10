import textwrap

from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class HelloRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path != '/':
            self.send_error(404, "Object not found")
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        fileresp = open("index.html","r");
        response_text = fileresp.read();
        self.wfile.write(response_text.encode('utf-8'))


server_address = ('', 8000)
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()

