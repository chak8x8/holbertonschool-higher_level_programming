#!/usr/bin/env python3

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

server_address = ("", 8000)
httpd = HTTPServer(server_address, SimpleAPI)
print("Starting server on port 8000...")
httpd.serve_forever()
