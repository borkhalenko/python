import socket
from settings import tt_name
from settings import server_ip
from settings import server_port
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, int(server_port)))
s.send(tt_name)
s.close()
