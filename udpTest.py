from udp.client import UDPClient
from udp.server import UDPServer

SERVER_NAME = '127.0.0.1'
PORT = 12000
BUFFER_SIZE = 2048

def startTestUDPServer():
	print('Start')
	server = UDPServer(PORT, BUFFER_SIZE)
	server.start()

def startTestUDPClient():
	print('Start')
	message = input("Input lowercase sentence: ")

	client = UDPClient(SERVER_NAME, PORT, message, BUFFER_SIZE)
	
	receivedMessage = client.start()

	print('Received message: ' + receivedMessage)
