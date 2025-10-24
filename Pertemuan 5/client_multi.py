import socket
import threading

HOST = '127.0.0.1'
PORT = 6000

def client_thread(n):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            message = f"Request dari client {n}"
            s.sendall(message.encode())
            response = s.recv(1024).decode()
            print(f"Client {n} menerima: {response}")
    except Exception as e:
        print(f"Client {n} gagal: {e}")

threads = []
for i in range(10):
    t = threading.Thread(target=client_thread, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
