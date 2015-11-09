# 
# coding:utf-8
# 

'''
使用 @property
'''

__author__ = 'JyHu'


class Student(object):

	# getter 方法
	@property
	def score(self):
	    return self._score
	
	# setter 方法
	@score.setter
	def score(self, value):
		try:
			if not isinstance(value, int):
				raise ValueError('Score must be an integer')
			if value < 0 or value > 100:
				raise ValueError('Score must between 0 ~ 100')
			self._score = value
		except ValueError, error:
			print('Receive error : %s' % error)


	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		try:
			if len(value) > 10:
				raise ValueError('Name string is too long')
			if len(value) < 4:
				raise ValueError('Name string is too short')
		except ValueError, error:
			print('Receive error : %s' % error)
		self._name = value

	@property
	def birth(self):
	    return self._birth
	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
	    return 2015 - self._birth


s = Student()
s.score = 60
print(s.score)
s.score = 999
s.score = -1
s.name = 'Michael'
print(s.name)
s.name = 'Joy'
s.name = 'Michael Joson'
s.birth = 1991
print(s.age)







#
# work
# 

class Screen(object):

	# width 		setter、getter

	@property
	def width(self):
	    return self._width

	@width.setter
	def width(self, w):
	  	try:
	  		if w <= 0:
	  			raise ValueError('Length error ...')
	  		self._width = w
	  	except ValueError, error:
	  		print('width error : %s' % error) 
	

	# height 		setter、getter

	@property
	def height(self):
	    return self._height
	
	@height.setter
	def height(self, h):
		try:
			if h <= 0:
				raise ValueError('Length error ....')
			self._height = h
		except ValueError, error:
			print('height error : %s' % error)


	# resolution	getter

	@property
	def resolution(self):
	    return self._width * self._height

s = Screen()
s.width = 1280
s.height = 720
print(s.resolution)





