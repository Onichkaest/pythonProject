#  functional programming
def no_parameters():
    #  print('Hello world')
    return 'Hello World!'


print(no_parameters())  # Hello World!

def squares(number):
    return number ** 2


print(no_parameters())

print(squares(20) - 140)  # 260


def squares(number1, number2):
    return number1 ** number2
    # if number < 0:
    #     return number ** 3
    # else:
    #     return number ** 2

print(squares(5, 3))  # 125


def print_message(name, age, profession):
    print(f'Hello {name}. You are {age} years old. You work as {profession}.')
print_message('Roman', '34', 'Lector')

people = [('Roman', 34, 'Lector'), ('Jack', 25, 'Mechanic')]
for person in people:
    print_message(person[0], person[1], person[2])

# a = []
# print(a.append(1))
