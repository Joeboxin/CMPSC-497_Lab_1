import socket
HOST = "127.0.0.1"
PORT = 4009
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)
    s.close()

print(f"Received {str(data)}")