from socket import *

class TCPClient:
    def __init__(self, serverName, serverPort, message, bufferSize):
        self.serverPort = serverPort
        self.serverName = serverName
        self.message = message
        self.bufferSize = bufferSize

    def start(self):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((self.serverName, self.serverPort))

        socket.send(self.message.encode())

        modifiedMessage = socket.recv(self.bufferSize)

        clientSocket.close()

        return modifiedMessage