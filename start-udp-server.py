from udp.server import UDPServer
from serverEnv import SERVER_PORT, BUFFER_SIZE

print('Start')
server = UDPServer(SERVER_PORT, BUFFER_SIZE)
server.start()
