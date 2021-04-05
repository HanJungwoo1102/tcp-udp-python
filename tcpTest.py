from tcp.client import TCPClient
from tcp.server import TCPServer

SERVER_NAME = '127.0.0.1'
PORT = 12000
BUFFER_SIZE = 2048

def startTestTCPServer():
	print('Start')
	server = TCPServer(PORT, BUFFER_SIZE)
	server.start()

def startTestTCPClient():
	print('Start')
	message = input("Input lowercase sentence: ")

	client = TCPClient(SERVER_NAME, PORT, message, BUFFER_SIZE)
	
	receivedMessage = client.start()

	print('Response message: ' + receivedMessage)
