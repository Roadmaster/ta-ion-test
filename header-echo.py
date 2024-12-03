#!/usr/bin/env python3
# A web server to echo back a request's headers and data.
from http.server import HTTPServer, BaseHTTPRequestHandler
import pprint
from threading import Thread
from socketserver import ThreadingMixIn
import socket

BIND_HOST = "::"
PORTS = [8080, 8443]


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.write_response(b"")

    def write_response(self, content):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(pprint.pformat(self.headers.items()).encode("utf-8"))
        self.wfile.write(b"\n")
        self.wfile.write(content)
        self.wfile.write(b"\n")
        print(content.decode("utf-8"))


class ThreadingHTTPServerV6(ThreadingMixIn, HTTPServer):
    address_family = socket.AF_INET6
    daemon_threads = True


def serve_on_port(port):
    server = ThreadingHTTPServerV6((BIND_HOST, port), SimpleHTTPRequestHandler)
    server.serve_forever()


print(f"Listening on http://{BIND_HOST}:{PORTS}\n")

Thread(target=serve_on_port, args=[PORTS[0]]).start()
serve_on_port(PORTS[1])
