'''
Name: UDPDocClient.py
Desc: Finds the required file and sends its contents to the server and that displays the calulated information
Auth: 1904021, Cameron Dunn
Date: 24/11/20
'''
import socket

#localhost and port number
SERVER_HOST = 'localhost'
SERVER_PORT = 54321

#stating the socket is transferiing TCP
CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to the server
CLIENT_SOCKET.connect((SERVER_HOST, SERVER_PORT))

#opens the txt file in read mode, reads it and then sends its contents to the server
OPENER = open("test.txt", "r")
if OPENER.mode == 'r':
    FILE_CONTENTS = OPENER.read()
    print("The file contents are: " + FILE_CONTENTS)
    CLIENT_SOCKET.sendall(FILE_CONTENTS.encode())

#takes the count and displays it
RECEIVED_MESSAGE, SERVER_ADDRESS = CLIENT_SOCKET.recvfrom(4096)
print (RECEIVED_MESSAGE.decode())

#takes the count and displays it
RECEIVED_MESSAGE, SERVER_ADDRESS = CLIENT_SOCKET.recvfrom(4096)
print (RECEIVED_MESSAGE.decode())

#closes the connection
CLIENT_SOCKET.close()