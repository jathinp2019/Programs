import socket

csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
num1 = input("Enter a number")
csock.sendto(num1.encode(), (socket.gethostname(), 6503))
data , addr = csock.recvfrom(4000)
print(data)
csock.close()