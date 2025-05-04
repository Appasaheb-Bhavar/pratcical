# #string formating
# name=input()
# age=input()
# print("hey my name is",name,"my age is",age)
#concatnetion
# first= (input())
# second=int(input())
# print(first+second)

import socket

HOST = 'localhost'  # Server IP address
PORT = 12345        # Server port number
FILE_PATH = 'D:/python program/aj.txt'  # Path of the file to be sent

def send_file():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        with open(FILE_PATH, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.sendall(data)

    print('File sent successfully.')

send_file()
