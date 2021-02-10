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
while True:#start while
    try:#input of the operation
        data = input("Insert operator, number one and number two to send (separated by a semicolon; 'E' for close the connection): ")
    except EOFError:
        print("\nOkay. Exit")
        break
    if not data:#start if; control if insert an empty string
        print("You can't send an empty string!")
        continue
    #end if
    if data == 'E' or data == 'e':#start if; control the closing connection case
        print("Closing the connection to the server!")
        break
    #end if
    data = data.encode()
    sock_service.send(data)
    data = sock_service.recv(2048)
    if not data:#start if
        print("Server does not respond. Exited")
        break
    #end if
    data = data.decode()#decoding the data
    print("Received from the server:")#printing the data received from the server
    print(data + '\n')
#end while
sock_service.close()
