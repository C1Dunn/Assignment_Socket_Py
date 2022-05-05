'''
Name: UDPCalcServer.py
Desc: Calulates the sum and sends it back
Auth: 1904021, Cameron Dunn
Date: 24/11/20
'''
import socket
#Defining the server port
SERVER_PORT = 12345
#Stating the sockets use UDP
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVER_SOCKET.bind(('localhost', SERVER_PORT))
#Confirmation to the user
print("The server is ready")
#Confirming the first number comes through successfully
INCOMING_MESSAGE, CLIENT_ADDRESS = SERVER_SOCKET.recvfrom(2048)
print("Incoming Message 1: ", INCOMING_MESSAGE)

#Confirming the second number (operator) comes through successfully
INCOMING_MESSAGE2, CLIENT_ADDRESS = SERVER_SOCKET.recvfrom(2048)
print("Incoming Message 2: ", INCOMING_MESSAGE2)

#Confirming the third number comes through successfully
INCOMING_MESSAGE3, CLIENT_ADDRESS = SERVER_SOCKET.recvfrom(2048)
print("Incoming Message 3: ", INCOMING_MESSAGE3)

#If statement to control which maths happen
if (int(INCOMING_MESSAGE2) == 1):
    OUTGOING_MESSAGE = int(INCOMING_MESSAGE) + int(INCOMING_MESSAGE3)
elif (int(INCOMING_MESSAGE2) == 2):
    OUTGOING_MESSAGE = int(INCOMING_MESSAGE) - int(INCOMING_MESSAGE3)
elif (int(INCOMING_MESSAGE2) == 3):
    OUTGOING_MESSAGE = int(INCOMING_MESSAGE) * int(INCOMING_MESSAGE3)
elif (int(INCOMING_MESSAGE2) == 4):
    OUTGOING_MESSAGE = int(INCOMING_MESSAGE) / int(INCOMING_MESSAGE3)
else: 
    OUTGOING_MESSAGE = 'Error'

#confirmation of result
print("Outgoing Message: ", OUTGOING_MESSAGE)

#Changing of int/ float to a string for easier endcoding and sending back to client
OUTGOING_MESSAGE = str(OUTGOING_MESSAGE)
SERVER_SOCKET.sendto(OUTGOING_MESSAGE.encode(), CLIENT_ADDRESS)
#closing of socket connection
SERVER_SOCKET.close()