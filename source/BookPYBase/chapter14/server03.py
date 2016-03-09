#coding:utf-8




'''
使用了分叉技术的服务器
'''


from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer):
	pass

class Handler(StreamRequestHandler):
	def handl(self):
		addr = self.request.getpeername()
		print 'Got connection from', addr
		self.wfile.write('Thank you for connecting')
server = Server(('', 1234), Handler)
server.serve_forever()





