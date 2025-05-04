import socket
import os

HOST = 'localhost'  # Server IP address
PORT = 12345        # Server port number

def receive_file():
    # Take folder path as input from the user
    folder_path = 'D:/SQL PROJECT'

    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    # Construct full file path
    file_path = os.path.join(folder_path, 'received_file')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print('Waiting for connection...')
        
        client_socket, addr = server_socket.accept()
        print('Connected to:', addr)

        with client_socket:
            with open(file_path, 'wb') as file:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    file.write(data)

        print(f'File received successfully and saved to: {file_path}')

receive_file()
