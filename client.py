import socket

HOST = "127.0.0.1"  # server's hostname or ip address
PORT = 1024         # port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    print('Received:', data.decode('utf-8')) # had to fix w this line since the print statement after close wouldn't work
    s.close()

# print('Received', str(data), encoding='utf-8')