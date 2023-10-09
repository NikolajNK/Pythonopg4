import socket

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 7))

    for _ in range(3):
        operation = input("Enter operation (Random, Add, Subtract): ")
        tal1 = input("Enter tal1: ")
        tal2 = input("Enter tal2: ")
        
        request = f"{operation};{tal1};{tal2}"
        client_socket.send(request.encode('utf-8'))
        
        response = client_socket.recv(1024).decode('utf-8')
        print("Response:", response)

    client_socket.close()

if __name__ == "__main__":
    client()