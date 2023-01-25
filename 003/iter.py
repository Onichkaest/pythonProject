courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'Math']

for course in courses:
    print(course.upper())  # will show all in capitals


courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'Math']
for course in courses:
    if course == 'Math':
        print('I don\'t like Math!')
    else:
        print(course.upper())  # result: I don't like Math!

pairs = [[1, 'one'], [2, 'two'], [3, 'three']]
for pair in pairs:
    print(pair[0], pair[1])


pairs = [[1, 'one'], [2, 'two'], [3, 'three']]
for num, word in pairs:
    print(num)
    print(word)


#
pairs = [['Jack', 'Smith', 22], ['Mary', 'Gold', 25], ['Bob', 'Sumers', 35]]
for first, last, age in pairs:
    print(f'Hello {first} {last}. You are {age} years old!')
# # Hello Jack Smith. You are 22 years old!
# # Hello Mary Gold. You are 25 years old!
# # Hello Bob Sumers. You are 35 years old!


for num1 in range(10,21):
    print(num1)
# # 10
# # 11
# # 12
# # 13
# # 14
# # 15
# # 16
# # 17
# # 18
# # 19
# # 20

for num1 in range(10,21,2):
    print(num1)
# 10
# 12
# 14
# 16
# 18
# 20
for num1 in range(10):
    for num2 in range(10):
        for num3 in range(10):
            for num4 in range(10):
                print(num1, num2, num3, num4)
# #  will show all combinations of 0 to 9 in 4 digits
# # 0 0 0 0 to
# #  5 3 9 3
# #  5 3 9 4
# #  to 9 9 9 9
#
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
