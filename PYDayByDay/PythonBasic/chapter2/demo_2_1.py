#coding=utf-8
from pip._vendor.distlib.compat import raw_input

__author__ = 'JinyouHu'


edward = ['Edward Gumdy', 42]
print(edward[0])

print("Hello world"[3])
print("Nihao"[-3])

endings = ['st', 'nd', 'rd'] + 17 *['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
print(endings)
# year = raw_input('Year : ')
# month = raw_input('Month(1-12) : ')
# day = raw_input('Day(1-31) : ')
# day_number = int(day)
# print(month + ' ' + day + str(endings[day_number - 1]) + ' , ' + year)


tag = '<a href="http://www.baidu.com">baidu</a>'
print(tag[9:29])
print(tag[31:-4])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(numbers[6:9])
print(numbers[-3:-1])
print(numbers[-3:])
print(numbers[:3])

print(numbers[0:10:1])
print(numbers[::3])
print(numbers[8:3:-1])
print(numbers[::-1])

print([1, 2, 3] + [4, 5, 6])

print('python ' * 5)


sentence = raw_input("Sentence : ")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print()
print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
print(' ' * left_margin + '|' + ' ' * text_width      + '|')
print(' ' * left_margin + '|' +        sentence       + '|')
print(' ' * left_margin + '|' + ' ' * text_width      + '|')
print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')


print('w' in 'Jyhou')

numbers = [100, 34, 678]
print(len(numbers))
print(max(numbers))
print(min(numbers))
