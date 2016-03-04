#coding = utf-8

__author__ = 'JinyouHU'

#multi-way decision

x = int(raw_input('please enter an integer :'))
if x < 0:
    x = 0
    print 'negative changed to zero'
elif x == 0:
    print 'zero'
else:
    print 'more'

#loops list

a = ['cat', 'window', 'defenestrate']
for x in a:
    print x,len(x)