import socket

ssock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ssock.bind((socket.gethostname(), 6503))

num,addr = ssock.recvfrom(4000)

n = int(num)

n = n+10

num = str(n)
ssock.sendto(num.encode(),addr)

ssock.close()
