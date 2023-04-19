import socket

serversocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(),6503))
serversocket.listen()
conn , addr = serversocket.accept()

data = conn.recv(1024).decode()

def isPalindrome(s):
	return s == s[::-1]

ans = isPalindrome(data)
w=''
if ans:
    w='yes'
else:
    w='no'

prod = str(w)
conn.send(prod.encode())
conn.close()
serversocket.close()