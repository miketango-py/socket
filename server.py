#!/usr/bin/env python3
#https://realpython.com/python-sockets/
#import -- from
import socket
#variables
HOST = '127.0.0.1'  # Indirizzo dell'interfaccia standard di loopback (localhost)
PORT = 65432        # Porta di ascolto, la lista di quelle utilizzabili parte da >1023)
#code
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#start with (for creating AKA 'with <variable> as <aka>:')
    s.bind((HOST, PORT))#association to the host and port
    s.listen()#listening for connections
    print("[*]Listening on %s:%d" % (HOST, PORT))
    clientsocket, address = s.accept()#accepting connections; recieving the address and the client-socket
    with clientsocket as cs:#start with 
        print('Connection from', address)
        while True:#start while
            data = cs.recv(1024)
            if not data:#start if
                break
            #end if
            cs.sendall(data)
        #end while
    #end with
#end with