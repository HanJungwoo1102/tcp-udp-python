from tcp.client import TCPClient
from serverEnv import SERVER_NAME, SERVER_PORT, BUFFER_SIZE

print('Start')
message = input("Input lowercase sentence: ")

client = TCPClient(SERVER_NAME, SERVER_PORT, message, BUFFER_SIZE)

receivedMessage = client.start()

print('Response message: ' + receivedMessage)
