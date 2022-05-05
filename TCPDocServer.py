'''
Name: UDPDocServer.py
Desc: takes the contents of the required file and counts its word count and characters excluding spaces.
Auth: 1904021, Cameron Dunn
Date: 24/11/20
'''
import socket

#Defining the server port and host
SERVER_HOST = 'localhost'
SERVER_PORT = 54321

#Stating the sockets use TCP
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#creating the connection
SERVER_SOCKET.bind((SERVER_HOST, SERVER_PORT))
SERVER_SOCKET.listen()
INCOMING_CONNECTION, CLIENT_ADDRESS = SERVER_SOCKET.accept()

while True:
    #Takes the incoming data and puts it into a variable
    INCOMING_MESSAGE = INCOMING_CONNECTION.recv(4096)
    if not INCOMING_MESSAGE:
        break

    #a test to verify code
    print (INCOMING_MESSAGE)

    #Calculates the character count without spaces and sends it to the client
    CHAR_COUNT = len(INCOMING_MESSAGE) - str(INCOMING_MESSAGE).count(" ")
    INCOMING_CONNECTION.sendall((str(CHAR_COUNT)).encode())

    #Calculates the word count and sends it to the client
    WORD_COUNT = len(INCOMING_MESSAGE.split())
    INCOMING_CONNECTION.sendall((str(WORD_COUNT)).encode())

#closes the connection
SERVER_SOCKET.close()