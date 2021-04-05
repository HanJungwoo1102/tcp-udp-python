from tcp.server import TCPServer
from serverEnv import SERVER_PORT, BUFFER_SIZE

print('Start')
server = TCPServer(SERVER_PORT, BUFFER_SIZE)
server.start()