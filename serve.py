#!/usr/bin/env python3
"""Run this, then open http://localhost:8000 in your browser."""
import http.server, socketserver
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}  (Ctrl+C to stop)")
    httpd.serve_forever()
