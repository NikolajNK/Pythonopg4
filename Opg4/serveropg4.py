import socket
import threading
import random

def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024).decode('utf-8')
        if not request:
            break
        operation, tal1, tal2 = request.split(";")
        tal1, tal2 = int(tal1), int(tal2)
        
        if operation == "Random":
            response = str(random.randint(tal1, tal2))
        elif operation == "Add":
            response = str(tal1 + tal2)
        elif operation == "Subtract":
            response = str(tal1 - tal2)
        else:
            response = "Invalid Operation"
        
        client_socket.send(response.encode('utf-8'))
    client_socket.close()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 7))
    server_socket.listen(5)
    print("Server is listening")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    server()