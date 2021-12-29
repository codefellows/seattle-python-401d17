from http.server import BaseHTTPRequestHandler
import json
from http.server import HTTPStatus


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        datalen = int(self.headers["Content-Length"])
        data = self.rfile.read(datalen)
        obj = json.loads(data)
        print("Got object: {}".format(obj))
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        message = json.dumps(obj)
        self.wfile.write(message.encode())
