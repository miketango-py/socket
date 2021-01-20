#!/usr/bin/env python3
#https://realpython.com/python-sockets/
#import -- from
import socket
#variables
HOST = '127.0.0.1'  # Indirizzo dell'interfaccia standard di loopback (localhost)
PORT = 65433       # Porta di ascolto, la lista di quelle utilizzabili parte da >1023)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#code
# Optionale: permette di riavviare subito il codice,
# altrimenti bisognerebbe aspettare 2-4 minuti prima di poter riutilizzare(bindare) la stessa porta
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
print("[*] Listening on %s:%d" % (HOST, PORT))
clientsocket, address = s.accept()
with clientsocket as cs:#start with
    print('Connection from', address)
    while True:#start while
        dati = cs.recv(1024)
        dati.decode()
        if not dati:#start if
            break
        #end if
        dati = dati.decode()
        print("Riceived '%s' from client" % dati)
        dati = "Hi, " + str(address) + ". I received this: '" + dati + "'"
        dati = dati.encode()
        # Invia i dati modificati al client
        cs.send(dati)
        print('Send to the client:', dati)
    #end while
#end with