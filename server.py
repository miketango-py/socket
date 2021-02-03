#!/usr/bin/env python3
#from -- import
import socket
#variables
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
sock_listen = socket.socket()
#code
sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
sock_listen.listen(5)
print("Server listening on: %s" % str((SERVER_ADDRESS, SERVER_PORT)))
while True:
    sock_service, addr_client = sock_listen.accept()
    print("\nConnection received from " + str(addr_client))
    print("\nWaiting for receive data ")
    contConn=0
    while True:
        data = sock_service.recv(2048)
        contConn+=1
        if not data:
            print("End data client. Reset")
            break
        
        data = data.decode()
        print("Received: '%s'" % data)
        if data=='0':
            print("Closing connection with: " + str(addr_client))
            break

        separator = data.split(';')
        if separator[0] == "piu":
            ris = (float(separator[1]) + float(separator[2]))

        if separator[0] == "meno":
            ris = (float(separator[1]) - float(separator[2]))
        
        if separator[0] == "per":
            ris = (float(separator[1]) * float(separator[2]))

        if separator[0] == "divisione":
            if separator[2] == 0:
                ris = "Is not possible to divide for '0'"
            else:
                ris = (float(separator[1]) / float(separator[2]))

        data = "Answer to: " + str(addr_client) + ".\n The result between " + str(separator[1]) + " and " + str(separator[2]) + " with the " + str(separator[0]) + " is: " + str(ris)
        data = data.encode()
        sock_service.send(data)

    sock_service.close()