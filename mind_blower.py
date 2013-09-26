#!/usr/bin/python

import socket   #for sockets
import sys  #for exit



try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'

host = '127.0.0.1'
port = 13854

s.connect((host, port))

print 'Socket Connected to ' + host + ' at port %d.' % port

while 1:
	byte = s.recv(1)
	if byte == 0xaa:
		byte = s.recv(1)
			if byte == 0xaa:
				packet_length = s.recv(1)
				if 