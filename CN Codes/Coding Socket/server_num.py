import socket

serversocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(),6503))
serversocket.listen()
conn , addr = serversocket.accept()


sum = 0
final = 0
while(True):
    num1 = conn.recv(1024).decode()
    if(num1 == "end"):
        break
    num1 = int(num1) 
    final += num1
    print(num1)
    sum = str(final)

    conn.send(sum.encode())

conn.close()
serversocket.close()