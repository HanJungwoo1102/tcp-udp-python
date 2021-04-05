from tcp.client import TCPClient
from tcp.server import TCPServer

PORT = 12000
BUFFER_SIZE = 2048

def startTCPServer():
	print('start')
	server = TCPServer(PORT, BUFFER_SIZE)
	server.start()

def startTCPClient():
	print('start')
	message = input("Input lowercase sentence:")

	client = TCPClient('127.0.0.1', PORT, message, BUFFER_SIZE)
	
	returnMessage = client.start()

	print('return message: ' + returnMessage)
