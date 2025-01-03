import socket

server_addres = ('192.168.0.102', 6666)
max_size = 1000

print('Starting the server\n')
print('Waiting for a client to call.\n')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_addres)
server.listen(5)
client, addr = server.accept()

while True:
    data = client.recv(max_size)
    print(data)
    print(type(data))
    if data == b"exit":
        break
    else:
        continue


client.close()
server.close()