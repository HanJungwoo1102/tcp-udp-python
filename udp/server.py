from socket import *

class UDPServer:
	def __init__(self, port, bufferSize):
		self.port = port
		self.bufferSize = bufferSize

	def start(self):
		serverSocket = socket(AF_INET, SOCK_DGRAM)

		serverSocket.bind(('', self.port))

		print("The server is ready to receive.")

		try:
			while True:
				message, clientAddress = serverSocket.recvfrom(self.bufferSize)
				modifiedMessage = message.decode().upper()

				serverSocket.sendto(modifiedMessage.encode(), clientAddress)
		except KeyboardInterrupt:
			print("Press Ctrl-C to terminate while statement")
			pass