#!/usr/bin/env python3
#from -- import
import socket
#variables
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
sock_service = socket.socket()
sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
#code
print("Connected to: " + str((SERVER_ADDRESS, SERVER_PORT)))
while True:
    try:
        data = input("Insert operator, number one and number two to send (separated by a semicolon; 'E' for close the connection): ")
    except EOFError:
        print("\nOkay. Exit")
        break
    if not data:
        print("You can't send an empty string!")
        continue
    if data == 'E' or data == 'e':
        print("Closing the connection to the server!")
        break

    data = data.encode()
    sock_service.send(data)
    data = sock_service.recv(2048)
    if not data:
        print("Server does not respond. Exited")
        break

    data = data.decode()
    print("Received from the server:")
    print(data + '\n')

sock_service.close()