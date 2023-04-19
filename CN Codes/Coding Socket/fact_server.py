import socket

serversocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(),6503))
serversocket.listen()
conn , addr = serversocket.accept()

data = conn.recv(1024).decode()
prod = 1
num = int(data)
while(num >= 1):
    prod = prod * num
    num = num -1
prod = str(prod)
conn.send(prod.encode())
conn.close()
serversocket.close()