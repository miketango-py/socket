#!/usr/bin/env python3
#import -- from
import socket
#variables
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
#code
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#start with
    s.connect((HOST, PORT))#connect to the host
    s.sendall(b'Socket connection successful!')#sending the msg (coded in byte (b))
    data = s.recv(1024)#listening for the answer
#end with
print(data.decode())#printing the recieved message