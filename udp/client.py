from socket import *

class UDPClient:
	def __init__(self, serverName, serverPort, message, bufferSize):
		self.serverPort = serverPort
		self.serverName = serverName
		self.message = message
		self.bufferSize = bufferSize
	
	def start(self):
		clientSocket = socket(AF_INET, SOCK_DGRAM)
		clientSocket.sendto(self.message.encode(), (self.serverName, self.serverPort))
		receivedMessage, serverAddress = clientSocket.recvfrom(self.bufferSize)
		clientSocket.close()
		
		return receivedMessage.decode()
		