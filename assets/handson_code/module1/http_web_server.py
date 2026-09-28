"""
PCCST501 Computer Networks - Module 1 Hands-on
Multi-threaded HTTP 1.1 Web Server in Python
Demonstrates HTTP request parsing, status codes (200, 404), MIME types, and TCP socket handling.
Author: Prof. Anju Markose | Dept. of CSE, VJCET
"""

import socket
import threading
import os
import mimetypes
from datetime import datetime

HOST = '127.0.0.1'
PORT = 8080
DOC_ROOT = './www_root'

def handle_client(client_socket, client_address):
    print(f"[+] Connection accepted from {client_address[0]}:{client_address[1]}")
    try:
        request_data = client_socket.recv(4096).decode('utf-8', errors='ignore')
        if not request_data:
            return

        # Parse HTTP Request Line (e.g., "GET /index.html HTTP/1.1")
        lines = request_data.split("\r\n")
        request_line = lines[0]
        print(f"[*] Request Line: {request_line}")

        tokens = request_line.split()
        if len(tokens) < 2:
            return

        method, path = tokens[0], tokens[1]
        
        if path == "/":
            path = "/index.html"
            
        file_path = os.path.join(DOC_ROOT, path.lstrip("/"))

        if os.path.exists(file_path) and not os.path.isdir(file_path):
            with open(file_path, "rb") as f:
                body = f.read()
            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type or "application/octet-stream"
            
            response_headers = [
                "HTTP/1.1 200 OK",
                f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}",
                "Server: VJCET-PyHTTP/1.0",
                f"Content-Type: {mime_type}",
                f"Content-Length: {len(body)}",
                "Connection: close",
                "\r\n"
            ]
            response = "\r\n".join(response_headers).encode('utf-8') + body
        else:
            body = b"<html><body><h1>404 Not Found</h1><p>Requested resource not found on VJCET CN Server.</p></body></html>"
            response_headers = [
                "HTTP/1.1 404 Not Found",
                f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}",
                "Server: VJCET-PyHTTP/1.0",
                "Content-Type: text/html",
                f"Content-Length: {len(body)}",
                "Connection: close",
                "\r\n"
            ]
            response = "\r\n".join(response_headers).encode('utf-8') + body

        client_socket.sendall(response)
    except Exception as e:
        print(f"[-] Error handling client {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"[-] Connection closed with {client_address}")

def start_server():
    os.makedirs(DOC_ROOT, exist_ok=True)
    index_file = os.path.join(DOC_ROOT, "index.html")
    if not os.path.exists(index_file):
        with open(index_file, "w") as f:
            f.write("<!DOCTYPE html><html><head><title>VJCET CN Server</title></head><body><h1>Welcome to PCCST501 HTTP Web Server!</h1><p>Testing HTTP 1.1 request-response pipeline.</p></body></html>")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(10)
    print(f"[*] HTTP Web Server running at http://{HOST}:{PORT}/")
    print("[*] Press Ctrl+C to stop server.")

    try:
        while True:
            client_sock, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(client_sock, addr), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        print("\n[*] Shutting down server gracefully...")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
