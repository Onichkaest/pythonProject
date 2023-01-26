#1
name = input('Please enter your name: ')
surname = input('Please enter your Surname: ')
age = input('Please enter your age: ')
print('Hello' + ' ' + str(name) + ' ' + str(surname) + '.' + ' ' + 'Your age is:' + ' ' + str(age))

#2
a = 2
b = 3
c = (a * a + b * b) ** 0.5
print(c)

#3
a = float(input('Please input the value of adjacent side: '))
b = float(input('Please input the value of opposite side: '))
c = float(input('Please input the value of adjacent hypotenuse: '))
if c ** 2 == a ** 2 + b ** 2:
    print('it is a right angle triangle')
else:
    print('not a right angle triangle')

#4
a = input('Please input a list element:')
b = input('Please input a list element:')
c = input('Please input a list element:')
list = [a, b, c]
print(list)
print(type(list))
list.reverse()
print(list)

#5
numbers = (1, 2, 3, 4)
numbers2 = (5, 6, 7)
print(type(numbers))
x = list(numbers)
x2 = list(numbers2)
print(x)
print(type(x))
print(x2)
print(type(x2))
number3= x + x2
print(number3)
