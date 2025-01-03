import socket

server_addres = ('localhost', 6789)
max_size = 1000

print('Starting the server\n')
print('Waiting for a client to call.\n')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_addres)
server.listen(5)
client, addr = server.accept()
kek = 0
while True:
    data = client.recv(max_size)
    print(f"At {client} said {data}")
    kek += 1
    if kek == 10:
        break
    else:
        continue

client.close()
server.close()