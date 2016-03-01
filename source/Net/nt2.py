#coding:utf-8


import socket

print 'Creating socket ...'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'done'


print 'loking up port number ..'
port = socket.getservbyname('http', 'tcp')
print 'done'

print 'connecting to remote host on port %d' % port
s.connect(('www.google.com', port))
print 'done'

print 'connected from ' + s.getsockname()
print 'connected to ' + s.getpeername() 