#!/usr/bin/env python3
#from -- import
import socket, sys, random, os, time
import threading, multiprocessing
#variables
SERVER_ADDRESS = '192.168.9.23'
SERVER_PORT = 22224
NUM_WORKERS = 15#numbers of threads generated automatically by the client
#functions
def generate_requests (SERVER_ADDRESS, SERVER_PORT):#start  generate_requests
    #variables
    #code
    start_time_thread = time.time()#taking the start time of the thread
    print("Client PID: {pid}, Process Name: {process_name}, Thread Name: {thread_name}"
            .format(pid = os.getpid(),#getting the PID of the process
            process_name = multiprocessing.current_process().name,#getting the name of the process
            thread_name = threading.current_thread().name)#getting the name of the thread
    )
    try:#start try -- except
        sock_service = socket.socket()#creating the client socket
        sock_service.connect((SERVER_ADDRESS, SERVER_PORT))#connecting to the server
        print("{thread_name} Connecting to the Server: {server_address}:{server_port}"#printing the info of the connection
                .format(thread_name = threading.current_thread().name,#getting the name of the thread
                server_address = SERVER_ADDRESS,#getting the server address
                server_port = SERVER_PORT)#getting the server port
                )
    except sock_service.error as socket_service_error:#error case
        print("{thread_name} Something gone wrong -> Error: {socket_service_error}"#printing an error output
                .format(thread_name = threading.current_thread().name,#getting the thread name
                socket_service_error = socket_service_error)#insert the socket service error
                )
        print("\nExiting...")
        sys.exit()#exiting the program
    #end try -- except
    commands = ['piu', 'meno', 'per', 'diviso']#calculator operators
    operation = commands[random.randint(0,3)]#generating randomly numbers between 0 and 3 (0 = piu; 1 = meno; 2 = per; 3 = diviso)
    data = str(operation) + ";" + str(random.randint(1,100)) + ";" + str(random.randint(1,100))#printing the operation and generating and printing the operators
    data = data.encode()#encoding data
    sock_service.send(data)
    data = sock_service.recv(2048)
    if not data:#start if; server doesn't response case
        print("{thread_name}: Server doesn't response. Exiting".format(thread_name = threading.current_thread().name))
    #end if
    data = data.decode()#decoding the data received
    print("{thread_name} Received from the Server: " + data + "\n"#printing the received data
            .format(thread_name = threading.current_thread().name)#getting the thread name
        )
    data = "E"#character for closing the connection
    data = data.encode()#encoding the data
    sock_service.send(data)#sending the data
    sock_service.close()
    end_time_thread = time.time()#taking the end time of the process
    print("{thread_name} Execution time: {exe_time}"
            .format(thread_name = threading.current_thread().name,#getting the thread name
            exe_time = end_time_thread - start_time_thread)#calculating the execution time (end time - start time = execution time)
        )
#end generate_requests
#code
if __name__ == '__main__':#start if
    #run tasks using processes
    start_time = time.time()#taking the start time of the process
    processes = [multiprocessing.Process(target = generate_requests, args = (SERVER_ADDRESS, SERVER_PORT))for _ in range(NUM_WORKERS)]
    [process.start() for process in processes]#starting the processes
    [process.join() for process in processes]#let the process wait  
    end_time = time.time()#taking the end time of the process
    print("{process_name} Execution time: {exe_time}"
            .format(process_name = multiprocessing.current_process().name,#getting the name of the process
            exe_time = end_time - start_time)#calculating the execution time = end_time - start_time
        )
#end if