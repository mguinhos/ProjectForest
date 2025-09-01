from http.server import HTTPServer, SimpleHTTPRequestHandler

class COOPHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Required for SharedArrayBuffer
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

if __name__ == "__main__":
    port = 8000
    httpd = HTTPServer(("localhost", port), COOPHandler)
    print(f"Serving on http://localhost:{port}")
    httpd.serve_forever()

