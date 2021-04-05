from tcp.client import TCPClient
from tcp.server import TCPServer

SERVER_NAME = '127.0.0.1'
PORT = 12000
BUFFER_SIZE = 2048

def startTestTCPServer():
	print('start')
	server = TCPServer(PORT, BUFFER_SIZE)
	server.start()

def startTestTCPClient():
	print('start')
	message = input("Input lowercase sentence: ")

	client = TCPClient('127.0.0.1', PORT, message, BUFFER_SIZE)
	
	receivedMessage = client.start()

	print('response message: ' + receivedMessage)
