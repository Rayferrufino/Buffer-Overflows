#!/usr/bin/python

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
string = 'test'

try:
    print "\n Sending evil buffer..."
    s.connect(('10.209.42.149', 110))
    data = s.recv(1024)
    print data

    s.send('USER test' + '\r\n')
    data = s.recv(1024)
    print data

    s.send('PASS ' + string + '\r\n')
    data = s.recv(1023)
    print data

    s.close()
    print "\nDone!"
except:
    print "Could not connect to POP3!"
