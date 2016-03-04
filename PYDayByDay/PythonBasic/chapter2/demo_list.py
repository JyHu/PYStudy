__author__ = 'JinyouHu'

print(list('hello'))
print(''.join(list('hello')))


x = [1, 2, 3, 4, 5, 6, 7]
x[0] = 4
print(x)
del x[2]
print(x)
x[4:] = [8, 9, 0]
print(x)
x[0:2] = [-2, -1, 0, 1, 2, 3]
print(x)
x[2:5] = []
print(x)
del x[1::3]
print(x)
x.append(4)
print(x)
print(x.count(4))
x.extend([10, 11, 12])
print(x)
print(x.index(10))
print(x[2])
x.insert(3, 'a')
print(x)
x.pop()
print(x)
x.pop(6)
print(x)
x.reverse()
print(x)
x.remove('a')
print(x)
x.sort(reverse=True)
print(x)
y = sorted(x)
print(y)