import socket

address = ("192.168.0.102", 6789)
max_size = 1000

print("starting the cleint\n")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
kek = 0
while True:
    sms = input("-->")
    client.sendall(bytes(sms, encoding="utf-8"))
    kek += 1
    if kek == 5:
        break
    else:
        continue
client.close()
