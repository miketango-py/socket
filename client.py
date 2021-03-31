#!/usr/bin/env python3
#from -- import
import socket

#variables
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

#           send    receive        send             receive
protocol = ["SYN", "ACK with Data"]
data = ""
#code
sock_service = socket.socket()
sock_service.connect((SERVER_ADDRESS, SERVER_PORT))

#printing the server data where the client is connected
print("Client connected to: " + str((SERVER_ADDRESS, SERVER_PORT)))

#ctrl the sended data
while True:
    try:
        choice = input("\n0 = SYN, 2 = ACK with Data\nInsert the data to send ('-1' for end the connection): ")
    except EOFError:
        print("\nOk. Exit")
        break

    #empty string case
    if not choice:
        print("You can't send an empty string!")
        continue
    
    #SYN case
    if choice == '0':
        choice = protocol[0]
        data = protocol[0]

    #ACK with Data case
    if choice == '2':
        choice = protocol[1]
        data = protocol[1]

    #closing connection case
    if choice == '-1':
        print("Closing the connection to the server!")
        break

    choice = choice.encode()
    sock_service.send(choice)

    choice = sock_service.recv(2048)

    if not choice:
        print("The server does not respond. Exit")
        break
    
    choice = choice.decode()

    print("Sended: " + data)
    print("\nReceived: "+ choice + '\n')

sock_service.close()