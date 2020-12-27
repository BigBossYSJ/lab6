import socket

ClientSocket = socket.socket()
host = '192.168.0.136'
port = 8888

print (' Waiting for connection')

try:
	ClientSocket.connect((host,port))

except socket.error as e:
	print(str(e))

Response = ClientSocket.recv(1024)
print (Response)

while True:

	Ipt = input('Say Something: ')
	ClientSocket.send(str.encode(Ipt))
	Response = ClientSocket.recv(1024)
	print (Response.decode('utf-8'))

ClientSocket.close()
