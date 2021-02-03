#!/usr/bin/env python3
import socket



SERVER_ADDRESS = '127.0.0.1'

SERVER_PORT = 22224

sock_listen = socket.socket()

sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))

sock_listen.listen(5)

print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))


while True:
    sock_service, addr_client = sock_listen.accept()
    print("\nConnection recieved from " + str(addr_client))
    print("\nWaiting for recieving data ")
    contConn=0
    while True:
        dati = sock_service.recv(2048)
        contConn+=1
        if not dati:
            print("End data client. Reset")
            break
        
        dati = dati.decode()
        print("Ricieved: '%s'" % dati)
        if dati=='0':
            print("Closing the connection with " + str(addr_client))
            break
        dati = "Answer to : " + str(addr_client) + ". The value of the counter is: " + str(contConn)

        dati = dati.encode()

        sock_service.send(dati)

    sock_service.close()