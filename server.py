#!/usr/bin/env python3
import socket

#variables
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

#code
sock_listen = socket.socket()
sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
sock_listen.listen(5)
print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))

while True:
    sock_service, addr_client = sock_listen.accept()
    print("\nConnection recieved from " + str(addr_client))
    print("\nWaiting for receiving data ")
    contConn=0
    while True:
        dati = sock_service.recv(2048)
        contConn+=1
        
        #if dati is empty
        if not dati:
            print("End data client. Reset")
            break

        #decoding the data received
        dati = dati.decode()
        
        #SYN case (0)
        if dati == 'SYN':
            print("Received: '%s'" % dati)
            data = "SYN + ACK"

        #ACK with Data case (2)
        if dati == 'ACK with Data':
            print("Received: '%s'" % dati)
            data = "ACK for Data"

        if dati=='-1':
            print("Closing the connection with " + str(addr_client))
            break

        dati = dati.encode()

        sock_service.send(dati)

    sock_service.close()