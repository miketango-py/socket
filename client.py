#!/usr/bin/env python3
#import -- from
import socket
#variables
SERVER_ADDRESS = '127.0.0.1'  # The server's hostname or IP address
SERVER_PORT = 65433        # The port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#code
s.connect((SERVER_ADDRESS, SERVER_PORT))
data = input("Insert the message for the server: ")
data = data.encode()
# Send data to server
s.send(data)
# Receive response from server
data = s.recv(2048)
if data:#start if
    # Convert back to string for python3
    data = data.decode()
    print("I received from the server: ")
    print(data + '\n')
#end if