from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        obj = {"name": "Jason"}
        message = json.dumps(obj)
        self.wfile.write(message.encode())
        return
