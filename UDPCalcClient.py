'''
Name: UDPCalcClient.py
Desc: Takes user input to send to the server for calculation and then outputs result
Auth: 1904021, Cameron Dunn
Date: 24/11/20
'''
import socket
#localhost and port number
SERVER_NAME = 'localhost'
SERVER_PORT = 12345

#stating the socket is transferiing UDP
CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Text output to the user
USER_MESSAGE = input("Please input the first number\n")
#sends response the server after encoding it to bytes
CLIENT_SOCKET.sendto(USER_MESSAGE.encode(), (SERVER_NAME, SERVER_PORT))

#Text output to the user
USER_MESSAGE2 = input("Please input the operator number: (1 for +, 2 for -, 3 for *, 4 for /)\n")
#sends response the server after encoding it to bytes
CLIENT_SOCKET.sendto(USER_MESSAGE2.encode(), (SERVER_NAME, SERVER_PORT))

#Text output to the user
USER_MESSAGE3 = input("Please input the second number\n")
#sends response the server after encoding it to bytes
CLIENT_SOCKET.sendto(USER_MESSAGE3.encode(), (SERVER_NAME, SERVER_PORT))

#takes the recieved data from the server and prints it out
MODIFIED_MESSAGE, SERVER_ADDRESS = CLIENT_SOCKET.recvfrom(2048)
print(MODIFIED_MESSAGE.decode())
#closes the connection
CLIENT_SOCKET.close()