a = 1
b = 2
c = 3

def tester(a, b, c):
    a = 10
    b = 20
    c = 30
    print(a, b, c)

print(a, b, c)  # 1 2 3
tester(a, b, c)  # 10 20 30

def test123(a, b, c=1):
    return a * b * c


print(test123(10, 5, 3))  # 150


def test123(a, b, d, c=1):
    return a * b * c * d


print(test123(10, 5, 3))  # 150
print(test123(d=3, b=5, a=11))  # 165


def tester(a, b=1, *args):  # no more than 4, but if need more
    print(a, b)  # returned after wrote tester line below
    print(args)  # 'hello'....
    for arg in args:
        print(arg)


tester(1, 1, 'hello', 123, True, False, None, 0.123, 'hello again!')


def say_hello():
    print('Hello')  # prints Hello


def take_name(name):
    say_hello()
    print(name)  # takes name from below


take_name('Roman')


def wrapper(f):
    print('Starting work')
    f()
    print('Ending work')


wrapper(say_hello)
# Starting work
# Hello
# Ending work


