#!/usr/bin/env python3
import argparse
import contextlib
import functools
import http.server
import socketserver
import threading
import time
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def fetch(host, port, path):
    with urlopen(f"http://{host}:{port}{path}", timeout=5) as response:
        response.read(64)
        return response.status, response.headers.get_content_type()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    handler = functools.partial(QuietHandler, directory=str(ROOT))
    try:
        httpd = ReusableTCPServer((args.host, args.port), handler)
    except OSError:
        # A developer may already be running `make serve` on PORT.
        # For smoke tests, falling back to an ephemeral port is safer than failing.
        httpd = ReusableTCPServer((args.host, 0), handler)

    with httpd:
        args.port = httpd.server_address[1]
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        time.sleep(0.2)

        expected = {
            "/": "text/html",
            "/assets/css/styles.css": "text/css",
            "/assets/js/main.js": "text/javascript",
            "/assets/images/logo.png": "image/png",
            "/assets/images/inline-01.jpg": "image/jpeg",
            "/robots.txt": "text/plain",
            "/sitemap.xml": "application/xml",
        }

        for path, content_type in expected.items():
            status, got = fetch(args.host, args.port, path)
            if status != 200:
                raise SystemExit(f"{path}: expected 200, got {status}")
            if got != content_type:
                raise SystemExit(f"{path}: expected {content_type}, got {got}")
            print(f"{path} {status} {got}")

        httpd.shutdown()

    print("smoke=ok")


if __name__ == "__main__":
    main()
