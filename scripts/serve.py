#!/usr/bin/env python3
"""Serve an HTML deck locally with explicit UTF-8 headers."""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class UTF8Handler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".html": "text/html; charset=utf-8",
        ".css": "text/css; charset=utf-8",
        ".js": "text/javascript; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".svg": "image/svg+xml; charset=utf-8",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve an HTML PPT folder with UTF-8 headers.")
    parser.add_argument("directory", nargs="?", default=".", help="Folder containing the deck")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--bind", default="127.0.0.1")
    args = parser.parse_args()

    directory = Path(args.directory).resolve()
    if not directory.is_dir():
        parser.error(f"not a directory: {directory}")

    handler = partial(UTF8Handler, directory=str(directory))
    server = ThreadingHTTPServer((args.bind, args.port), handler)
    print(f"Serving {directory} at http://{args.bind}:{args.port}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
