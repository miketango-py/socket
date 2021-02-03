#!/usr/bin/env python3


input_string = 'Hello'
print(type(input_string))
input_bytes_encoded = input_string.encode()
print(type(input_bytes_encoded))
print(input_bytes_encoded)
output_string=input_bytes_encoded.decode()
print(type(output_string))
print(output_string)

import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

sock_service = socket.socket()

sock_service.connect((SERVER_ADDRESS, SERVER_PORT))

print("Connect to " + str((SERVER_ADDRESS, SERVER_PORT)))
while True:
    try:
        dati = input("Insert the data to send ('0' for end the connection): ")
    except EOFError:
        print("\nOk. Exit")
        break
    if not dati:
        print("You can't send an empty string!")
        continue
    if dati == '0':
        print("Closing the connection to the server!")
        break
    
    dati = dati.encode()

    sock_service.send(dati)

    dati = sock_service.recv(2048)

    if not dati:
        print("The server does not respond. Exit")
        break
    
    dati = dati.decode()

    print("Recieved from the server:")
    print(dati + '\n')

sock_service.close()