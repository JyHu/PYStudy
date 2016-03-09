#coding:utf-8


'''
一个基于SocketServer的小型服务器
'''


from SocketServer import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):
	def handle(self):
		addr = self.request.getpeername()
		print 'Got connection from ', addr
		self.wfile.write('Thank you for connection')
server = TCPServer(('', 1234), Handler)
server.serve_forever()



