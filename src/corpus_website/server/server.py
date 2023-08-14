from typing import Callable
from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path
from functools import partial


class Server():

    def __init__(self, output_folder_path: Path, port: int):
        self.output_folder_path = output_folder_path
        self.port = port

    def serve(self, reload_callback: Callable[[], None]) -> None:

        output_folder_path = self.output_folder_path
        
        class Handler(SimpleHTTPRequestHandler):
            
            def __init__(self, request, client_address, server):
                super().__init__(request, client_address, server, directory=output_folder_path)

            def do_GET(self):
                reload_callback()
                super().do_GET()

        # Bind to the local address only.
        server_address = ("127.0.0.1", self.port)
        httpd = HTTPServer(server_address, Handler)
        httpd.serve_forever() 