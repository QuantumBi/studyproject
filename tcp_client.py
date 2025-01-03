import socket

address = ("192.168.0.102", 6789)
max_size = 1000

print("starting the cleint\n")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'Hey!')
data = client.recv(max_size)
print("at someone replied", data)
client.close()
