import socket
import sys
import os

cl = socket.socket()
host = '192.168.0.136'
port = 8888

try:
	cl.connect((host,port))
	print('Connection Successfull')
except socket.error as e:
	print (str(e))

while True:
	print('Hi!, This is Python Calculator')
	print('1-Log expression')
	print('2-Square root expression')
	print('3-Exponential expression')
	print('0-exit')

	ans = input('Enter your expressions choices:')
	cl.send(ans.encode())
	os.system('clear')
	if ans == '1':
		#log
		print('Log function!')
		num=input('Enter any number:')
		b = input('Enter any base:')
		cl.send(num.encode())
		cl.send(b.encode())
		total=cl.recv(1024)

		print('The answer is :'+ str(total.decode('utf-8')))
	elif ans == '2':
		# root
		cod = True
		while cod:
			print('Square root function!')
			num =input('Enter any number:')
			if int(num)> -1:
				cod = False
				cl.send(num.encode())
				total=cl.recv(1024)
			else:
				print('Enter any positive number')

		print('The answer is :'+ str(total.decode('utf-8')))

	elif ans == '3':
		#exponen
		print('Exponential function!')
		num=input('Enter any number:')
		cl.send(num.encode())
		total=cl.recv(1024)
		print('The answer is :'+ str(total.decode('utf-8')))

	elif ans == '0':
		#eixt

		cl.close()
		sys.exit()
	else:
		print('Input Denied!')
