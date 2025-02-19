#!/usr/bin/python3
"""
This module fetches posts from a RESTful API and prints them to the console
or saves them to a file.
"""


import http.server
import json


class RequestHandler(http.server.BaseHTTPRequestHandler):
    """
    This class handles HTTP requests
    """
    def do_GET(self):
        """
        Handles GET requests
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, RequestHandler)
    print("Starting server on port 8000...")
    httpd.serve_forever()
