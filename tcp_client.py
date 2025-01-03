import socket

address = ("192.168.0.102", 6789)
max_size = 1000

print("starting the cleint\n")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
kek = 0
while True:
    client.sendall(bin(str(input("-->"))))
    data = client.recv(max_size)
    kek += 1
    if kek == 5:
        break
    else:
        continue
client.close()
