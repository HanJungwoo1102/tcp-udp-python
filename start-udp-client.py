from udp.client import UDPClient
from serverEnv import SERVER_NAME, SERVER_PORT, BUFFER_SIZE

print('Start')
message = input("Input lowercase sentence: ")

client = UDPClient(SERVER_NAME, SERVER_PORT, message, BUFFER_SIZE)

receivedMessage = client.start()

print('Received message: ' + receivedMessage)
