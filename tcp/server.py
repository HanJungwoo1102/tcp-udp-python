from socket import *

class TCPServer:
	def __init__(self, port, bufferSize):
		self.port = port
		self.bufferSize = bufferSize

	def start(self):
		serverSocket = socket(AF_INET, SOCK_STREAM)

		serverSocket.bind(('', self.port))

		serverSocket.listen(1)

		try:
			while True:
				connectionSocket, clientAddress = serverSocket.accept()
				message = connectionSocket.recv(self.bufferSize)
				modifiedMessage = message.decode().upper()
				connectionSocket.send(modifiedMessage.encode())
				connectionSocket.close()
		except KeyboardInterrupt:
			print("Press Ctrl-C to terminate while statement")
			pass