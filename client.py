#!/usr/bin/env python3
#import -- from
import socket
#variables
SERVER_ADDRESS = '127.0.0.1'  # The server's hostname or IP address
SERVER_PORT = 65433        # The port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#code
s.connect((SERVER_ADDRESS, SERVER_PORT))
dati = input("Insert the message for the server: ")
dati = dati.encode()
# Send data to server
s.send(dati)
# Receive response from server
dati = s.recv(2048)
if dati:#start if
    # Convert back to string for python3
    dati = dati.decode()
    print("I received from the server: ")
    print(dati + '\n')
#end if