#!/usr/bin/env python3
#from -- import
import socket

#variables
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

#           send    receive        send             receive
protocol = ["SYN", "SYN ACK", "ACK with Data", "ACK for Data"]
step = 0#steps of the communication
data = ""
#code
sock_service = socket.socket()
sock_service.connect((SERVER_ADDRESS, SERVER_PORT))

#printing the server data where the client is connected
print("Client connected to: " + str((SERVER_ADDRESS, SERVER_PORT)))

#assigning the steps to data (converting int to string)
data = str(step)

while True:
    try:
        choice = input("Insert the data to send ('-1' for end the connection): ")
    except EOFError:
        print("\nOk. Exit")
        break

    #empty string case
    if not choice:
        print("You can't send an empty string!")
        continue

    #closing connection case
    if choice == '-1':
        print("Closing the connection to the server!")
        break

    #sending SYN
    if choice == '0':
    choice = choice.encode()
    sock_service.send(choice)

    choice = sock_service.recv(2048)

    if not choice:
        print("The server does not respond. Exit")
        break
    
    choice = choice.decode()

    print("Received from the server:")
    print(choice + '\n')

sock_service.close()