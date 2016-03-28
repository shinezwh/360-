#!/usr/bin/python

import socket
import threading,sys,string

port=8000
list=50
dic={}
def varDefine():
	print "你可以定义变量, 例如: foo=2016"
	while True:
		str=raw_input()
		result=str.split('=')
		dic[result[0].strip()]=result[1].strip()


def handle(client,address):
	try:
		client.settimeout(400)
		buf=client.recv(1024)
		if buf in dic.keys():
			client.send(str(dic[buf]))
		else:
			client.send("%s 未定义，请先定义！ " % buf)
	except socket.timeout:
		print 'time out'
	client.close()


def main():

	thread=threading.Thread(target=varDefine)
	thread.start()

	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind(('localhost',port))
	sock.listen(list)
	
	while True:
		client,address = sock.accept()
		handleRequest = threading.Thread(target=handle,args=(client,address))
		handleRequest.start()





if __name__=="__main__":
	main()