__author__ = 'JinyouHU'



s = raw_input('input your age:')
if s == '':
    raise Exception('input must no be empty')
try:
    i = int(s)
except ValueError:
    print 'could not convert data to an integer'
except:
    print 'unknown exception!'
else:
    print "you are %d" %i,"years old"
finally:
    print 'good bye'