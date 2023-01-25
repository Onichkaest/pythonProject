string_sample1 = 'Hello world world'
                 #0123456789  -3 -2 -1
string_sample2 = 'first letteR is lowErcase'
string_sample3 = '     * * extra whitespaces * *    '
german_sample = 'der Fluß'

print(string_sample1[1])  # 1st letter (starts with 0)
print(string_sample1[-1])  # -1 from the end of sentence
print(string_sample1[6:11])  # 6 to 11 letters NOT including 11th
print(string_sample1[6:])  # if no end index then from 6th to end
print(string_sample1[:5])  # up to 4th
print(type(string_sample1[:]))

#[START:END:STEP]
print(string_sample1[::2])  # every second
print(string_sample1[-1:-6])  # will not work as always left to right
print(string_sample1[-6:])  # from -6 to end of sentence
print(string_sample1[::-1])  # will read right to left

print(len(string_sample1))  #17 symbols but starts with 0 so will show 16
print(string_sample1[len(string_sample1) - 1])

print(string_sample1.upper())  # will print in capitals
string_sample = string_sample1.upper()
print(german_sample.lower())  # in lowercase
print(german_sample.casefold())  # will convert to latin equivalent (ß will be ss)
print(len(german_sample.casefold()))  # will count letters including space in der fluss

print(string_sample1.isupper())  # if all capitals will be True
print(string_sample1.islower())  # if all lowercase will be True

print(string_sample2.capitalize())  # first word of the sentence will capitalise
print(string_sample2.title())  # all words will start with capital

print(string_sample3.strip())  # removes all spaces from sides
print(string_sample3.strip('* '))  # removes * and spaces
print(string_sample3.rstrip('* '))  # removes from right
print(string_sample3.lstrip('* '))  # removes from left

print(string_sample1.replace('world', 'planet'))  # finds 'world' and replaces with 'planet'
print(string_sample1.replace('world', 'planet', 1))  # will replace first "world" only
print(string_sample1.replace(' ', ''))  # finds all spaces and removes
print(string_sample1.replace(' ', '').replace('o', ''))  # will remove spaces & 'o's
print(string_sample1.split())  # will separate :       ['Hello', 'world', 'world']
print(string_sample1.split(' '))  # Converts to list with specified delimiter


c = 1, 2, 3
print(c)  # will return (1, 2, 3)
a, b, c = 1, 2, 3
print(c)  # will return 3

# a, b, c = input('Please enter 3 numbers using space: ').split()
# print(a)
# print(b)
# print(c)

print(string_sample1.count('o'))  # Will return number of times specified value occurs in string as (INT)
print(string_sample1.count('world'))  # will show how many times 'world' we have in the sentence
print(string_sample1.find('world'))  # first world starts with 6th index, gives 6 as result
print(string_sample1.find('world', 7))  # starting with 7th index will give 12 as that is when next world starts

print('world' in string_sample1)  # check if there is word "world" in that sample
# https://www.w3schools.com/python/python_ref_string.asp

a = 'Hello'
b = 'World'

print(a + ' ' + b)
print(a, b)
print(a, b, 12321, True, None)  # Hello World 12321 True None
print(a, b, 12321, True, None, sep='')  # sep is separator, in this case no space so will be HelloWorld12321TrueNone
print('fsgd\nfdh')  # will have fdh on the second line
txt = 'Hello\nWorld'
print(txt)
# print('that's')     will give error
print('that\'s')   # will work and show "that's"
# print("my favourite book is "Metro2033"")    will give error
print("my favourite book is \"Metro2033\"")
print('''That's''')  # will work
print(""" "Metro2033" """)
print(""" "Metro

2033" """)  # triple " will save formatting

salary = 2000
name = 'John'
age = 25
txt = '{} salary is {}. He is {} years old.'
print(txt.format(name, salary, age))  # John salary is 2000. He is 25 years old.

txt = '{2} salary is {2}. He is {2} years old.'

product = 'computer'
price = 1000
txt2 = 'This {prod:} costs {pr:}'
print(txt2.format(prod=product, pr=price))

txt2 = 'This {prod:} costs {pr:.2f}$'  # 2 decimals
print(txt2.format(prod=product, pr=price))  # This computer costs 1000.00$

x = 1234.123232
y = 123.1223
print('The value of x is %.4f'% x)  # 4 decimals   "The value of x is 1234.1232"

emp_name = 'John'
emp_age = 15
emp_salary = 1000


print(f'Hi, my name is {emp_name.upper()}. I am {emp_age + 10} years old. My salary is {emp_salary:.2f}.')

txt2 = 'Hello world!'
print(txt2.encode('utf-8'))
