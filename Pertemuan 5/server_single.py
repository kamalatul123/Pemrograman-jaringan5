import socket

HOST = '127.0.0.1'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server Single Thread berjalan di", (HOST, PORT))

while True:
    conn, addr = server_socket.accept()
    print("Terhubung dengan:", addr)
    data = conn.recv(1024).decode()
    print("Dari client:", data)
    conn.sendall(f"Server menerima: {data}".encode())
    conn.close()
