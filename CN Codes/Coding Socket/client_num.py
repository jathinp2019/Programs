import socket

csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csock.connect((socket.gethostname(),6503))

userinp = input("Enter the number or 'end'")
data = ""
while(userinp != "end"):
    csock.send(userinp.encode())
    data = csock.recv(1024).decode()
    print(data)
    userinp = input("Enter the next number or 'end'")

data = int(data)
print("The sum of numbers are ", data)

csock.close()