import socket

server_addres = ('192.168.0.102', 6789)
max_size = 1000

print('Starting the server\n')
print('Waiting for a client to call.\n')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_addres)
server.listen(5)

client, addr = server.accept()
data = client.recv(max_size)

print(f"At {client} said {data}")
client.sendall(b'Are you talking to me?')
client.close()
server.close()