#coding:utf-8



'''
一个使用了线程处理的服务器
'''

from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler

class Server(ThreadingMixIn, TCPServer):
	pass

class Handler(StreamRequestHandler):
	def handle(self):
		addr = self.request.getpeername()
		print 'Got connection from ', addr
		self.wfile.write('Thank you for connecting')

server =Server(('', 1234), Handler)
server.serve_forever()







