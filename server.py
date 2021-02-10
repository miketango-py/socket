#!/usr/bin/env python3
#from -- import
import socket
#variables
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
sock_listen = socket.socket()
#functions
def socket_listen(sock_listen, SERVER_ADDRESS, SERVER_PORT):#start socket_listen
    #variables
    #code
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
    sock_listen.listen(5)
    print("Server listening on: %s" % str((SERVER_ADDRESS, SERVER_PORT)))#taking and printing the info on the server
#end socket_listen
#code
socket_listen(sock_listen, SERVER_ADDRESS, SERVER_PORT)#calling the function socket_listen
while True:#start while
    sock_service, addr_client = sock_listen.accept()
    print("\nConnection received from " + str(addr_client))
    print("\nWaiting for receive data ")
    while True:#start while
        data = sock_service.recv(2048)
        if not data:#start if; control if the data is received or not
            print("End data client. Reset")
            break
        #end if
        data = data.decode()#decoding the data received
        print("Received: '%s'" % data)
        if data=='0':#start if; control data input, if 0 -> closing connection
            print("Closing connection with: " + str(addr_client))
            break
        #end if
        separator = data.split(';')
        if separator[0] == "piu":#start if; ctrl the operator with 'piu'
            ris = (float(separator[1]) + float(separator[2]))
        #end if
        if separator[0] == "meno":#ctrl the operator with 'meno'
            ris = (float(separator[1]) - float(separator[2]))
        #end if
        if separator[0] == "per":#ctrl the operator with 'per'
            ris = (float(separator[1]) * float(separator[2]))
        #end if
        if separator[0] == "diviso":#ctrl the operator with 'diviso'
            if separator[2] == '0':#ctrl the zero case (as number to be divided) 
                ris = str(separator[1]) + " / " + str(separator[2]) +  " is not possible"
                data = "Answer to: " + str(addr_client) + ".\n" + str(ris)
            else:
                ris = (float(separator[1]) / float(separator[2]))
            #end if - else
        #end if
        data = "Answer to: " + str(addr_client) + ".\n The result between " + str(separator[1]) + " and " + str(separator[2]) + " with the " + str(separator[0]) + " is: " + str(ris)
        data = data.encode()#encoding the data with the result
        sock_service.send(data)#sending the incoding data to the server
    #end while    
    sock_service.close()
#end while
    