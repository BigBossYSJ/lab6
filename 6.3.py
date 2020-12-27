import socket
import math
import errno
import sys
from multiprocessing import Process

def ProcessStart(server):
	while True:
		sel = server.recv(1024).decode()

		if sel == '1':
			#log calculation
			num = server.recv(3).decode()
			base = server.recv(2).decode()
			cal = math.log(float(num),float(base))

		elif sel == '2':
			#Squareroot calculation
			num = server.recv(1024).decode()
			cal = math.sqrt(float(num))

		elif sel == '3':
			#exponential calculation
			num = server.recv(1024).decode()
			cal = math.exp(float(num))

		elif sel == '0':
			#Close server
			server.close()
			break


		server.sendall(str(cal).encode())

if __name__ == '__main__':

	s = socket.socket()
	host = ''
	port = 8888

	try:
		s.bind((host,port))
		print('Waiting for connection')
	except socket.error as e:
		print (str(e))
		sys.exit()

	s.listen(5)
	while True:
		try:
			server,add = s.accept()
			print('Connection is successfull\n')

			p = Process(target = ProcessStart, args=(server,))
			p.start()

		except socket.error:
			print('Error detected!')

	s.close()
