empty_lst = list()
print(type(empty_lst))

world = 'world'
filled_lst = [123, 0.12345, True, 'Hello world!', [1, [9,9,9,], 3, 4]]  # list inside of list insid eof list
print(filled_lst)
print(len(filled_lst))  # 5 elements inside the list
print(filled_lst[1:4])  # [0.12345, True, 'Hello world!']
print(filled_lst[1:4:2])  # every second  [0.12345, 'Hello world!']
print(filled_lst[-1])  # [1, [9, 9, 9], 3, 4]
print(filled_lst[-1][1])  # [9, 9, 9]
print(filled_lst[-1][1][1])  # 9
filled_lst = [123, 0.12345, True, 'Hello world!', [1, [9, 'Hello World' , 9,9,], 3, 4]]
print(filled_lst[-1][1][1].upper())  # HELLO WORLD
print(filled_lst[-1][1][1][:5].upper())  # HELLO

courses = ['History', 'Math', 'Literature', 'Physics', 'Programming']
print(courses[::-1])  # razvorachivaet
nums = [1, 5, 6, 8, 3, 4, 2]
courses[1] = 'Art'  #pomenjali
print(courses)

courses.append('Art')  # added Art to list end
print(courses)
courses.extend(['Art', 'English'])  # more than one
print(courses)
courses.insert(0, 'English')  # insert in the beginning
print(courses)
print(courses[::-1])

courses.remove('Art')
print(courses)

courses = ['History', 'Math', 'Literature', 'Physics', 'Programming']
popped = courses.pop(0)  # deletes last
print(courses)
print(popped)  # will show Programming

courses.reverse()  # reverses courses
print(courses)
print(courses[::-1])
print(reversed(courses))
#
courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', '123']
courses.sort()  # sort courses  numbers then abc's etc
print(courses)

nums = [1, 5, 6, 8, 3, 4, 2]
nums.sort()
print(nums)
#
courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'art']
courses.sort(reverse=True)  # sort numbers in reverse
print(courses)
print(sorted(courses))

print(min(nums))  # minimum number from list
print(max(nums))
print(sum(nums))  # sum of all numbers from list
print(courses.index('Math'))  # 1 index where math is
print('Math' in courses)  # True checks if math is in there
print(8 in nums)  # True

courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'art']
courses_str = str(courses)
print(courses_str)
print(type(courses_str))
courses_str = ', '.join(courses)  # will become: History, Math, Literature, Physics, Programming
print(courses_str)
print(type(courses_str))
new_lst = courses_str.split(',')  # ['History, Math, Literature, Physics, Programming']
print(new_lst)
print(list('hello world'))  # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(courses + nums)  # ['History', 'Math', 'Literature', 'Physics', 'Programming', 1, 5, 6, 8, 3, 4, 2]
print(courses[:2] + nums[-3:])  # ['History', 'Math', 3, 4, 2]
#

courses2 = courses
a=5
b=a
a=2
print(a,b)
courses2 = courses  # below it will change in both
courses[0] = 'Art'
courses[1] = 'English'
print(courses)  # ['Art', 'English', 'Literature', 'Physics', 'Programming']
print(courses2)  # ['Art', 'English', 'Literature', 'Physics', 'Programming']

courses2 = courses.copy()  # now courses and courses 2 two different lists
print(id(courses))
print(id(courses2))

print(id(courses))
courses.append('Art')
print(id(courses))

courses = ('History', 'Math', 'Literature', 'Physics', 'Programming')
nums = (1, 5, 6, 8, 3, 4, 2)

empty_tup = tuple(courses)
print(empty_tup[0])  # will give History
print(empty_tup.index('Math'))  #1st
print(empty_tup.count('Math'))  # we have Math just 1 time so shows 1
print((1, 2, 3) + (4, 5, 6))
one = (1,)
print(one)
print(type(one))  # class tuple

courses = {'History', 'Math', 'Literature', 'Physics', 'Programming', 'Math'}
nums = {1, 5, 6, 8, 3, 4, 2}

empty_set = {}
print(empty_set)
print(type(empty_set))  # <class 'dict'>

print(courses)  # will get rid of duplicates
courses.remove('Math')
print(courses)

courses = {'History', 'Math', 'Literature', 'Physics', 'Programming', 'Math'}
nums = {1, 5, 6, 8, 3, 4, 2}
print(nums)
nums.remove(1)
print(nums)
courses = {'History', 'Math', 'Literature', 'Physics', 'Programming', 'Math'}
courses.remove('Math')
print(courses)
x = courses.pop()
print(courses)
print(x)

nums = {1, 5, 6, 8, 3, 4, 2}
nums.remove(1)
x = nums.pop()
print(nums)
print(x)  # will show 2 so last number

y = ['One', 'Two', 'Three', 'One', 'Two']
print(list(set(y)))

y = [4, 2, 5, 7, 1]
print(list(set(y)))  # [1, 2, 4, 5, 7]

courses = {'History', 'Math', 'Literature', 'Physics', 'Programming', 'Math'}
nums = {1, 5, 6, 8, 3, 4, 2}
courses.add('Art')
print(courses)  # will not have order

courses = {'History', 'Math', 'Literature', 'Physics', 'Programming', 'Math'}
nums = {1, 5, 6, 8, 3, 4, 2}
courses.update(['Art', 'English'])

set1 = {'Math', 'History', 'Physics', 'Art'}
set2 = {'Math', 'Literature', 'Physics', 'English'}

print(set1.union(set2))  # will join two and remove duplicates

set1 = {'Math', 'History', 'Physics', 'Art'}
set2 = {'Math', 'Literature', 'Physics', 'English'}
print(set1.intersection(set2))  # will show ones that are in both sets
print(set2.difference(set1))  # what set2 has that set1 does not {'Literature', 'English'}

x = [1, 2, 3]
y = [1, 2, 3]
print(x==y)  # true that one is same than other

x = (1, 2, 3)
y = (1, 2, 3)
print(x==y)

x = {1, 2, 3}
y = {1, 2, 3}
print(x==y)

x = [1, 2, 3]
print(str(x))  # [1, 2, 3]

x = []
print(bool(x))  # False. if number will be True

list()
tuple()
set()


