import socket

csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csock.connect((socket.gethostname(),6503))

userinp = input("Enter the string")

csock.send(userinp.encode())

data = csock.recv(1024).decode()

print(data)
csock.close()