import http.server
import socketserver
import os

port = 8080
os.chdir(os.path.dirname(__file__))

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(('', port), handler)
httpd.serve_forever()
