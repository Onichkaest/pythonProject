# # bla_bla_bla - can put # just to add comment for myself
a = 5
print(a)
print(type(a))  # integer (int) control+R to play

b = 0.123  # if number is .point something then return as float
print(b)
print(type(b))  # float (float)

c = 'Hello'
d = "World"
e = '''Hello'''
print(c)
print(type(c))  # string (str) meaning it is a word
print(len(c))  # checks how many letters/numbers in something
print(a == c)  # will show that it is false

true_val = True
false_val = False
print(true_val)
print(type(true_val))  # boolean (bool)

# none_val = None
# print(none_val)
# print(type(none_val))  # NoneType
#
print(round(1.5))  # rounds, if .5 then to nearest even number
print(round(2.5))

a = 200.123
b = 500
print(a + b * a)
#
str1 = 'Hello '
str2 = 'world'
print(str1 + str2)  # or can do +' '
#
# print(True + True)  # True is 1
#
# print(a - b)
#
print ('*' * 20)  # will produce ***********
#
# print(b/a)
print(b//a)  # rounds down the result
#
print(b % 30)  # ostatok pri delenii
#
print(b ** 2)  # b in the power of 2
#print(b**0.5)
#
# print((10+5)*2**2)  # power of 2 will be done first of not using brackets
#
int_val = 500
float_val = 50.9
string_num_val = "123.23"
string_text_val = "Hello World"
#
print(float(int_val))  # converted integer to float
print(int(float_val))  # convert float to integer
#
print(str(int_val))
print(type(str(int_val)))  # classified
#
print(string_text_val + str(int_val))
#
# print(int(string_num_val))  # cannot because it is a float
# print(int(float(string_num_val)))
# print(bool(1))
# print(bool('Hello World'))
# print(bool(0))  # false
# print(bool(''))  # false
# print(bool(None))  # false
#
# a = 5
# print(float(a))
# a = float(a)
#
