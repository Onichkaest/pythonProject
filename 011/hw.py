import re

colours = '''
#CD5C5C
#F08080
#FA8072
ABCDEFG
'''

numbers = '''
2*9-6*5
(3+5)-(9*4)
5+3=8
'''

breakfast = '''
Завтрак в 09:00
random 123:15
even more random 13:62
'''
# 1
pattern = re.compile(r'#[0-9A-F]{5}')
matches = pattern.finditer(colours)
for match in matches:
    print(match)

# 2
pattern = re.compile(r'[0-9]+[^+]')

matches = pattern.finditer(numbers)

for match in matches:
    print(match)

# 3 not sure :/

# 4

with open('people.txt', 'r', encoding='UTF8') as file:
    data = file.read()

pattern = re.compile(r'[A-Z][a-z]+ [A-Z][a-z]+[^St.|Vice City]')

matches = pattern.finditer(data)

for namesurname in matches:
    print(namesurname)

pattern = re.compile(r'\d{3} [A-Z][a-z]+ [A-Z][a-z]+')

matches = pattern.finditer(data)

for address in matches:
    print(address)

# 5
with open('people.txt', 'r', encoding='UTF8') as file:
    data = file.read()

pattern = re.compile(r'[\W_]')

matches = pattern.findall(data)
if len(matches) > 0:
    print ('строка состоит не только из символов')
else:
    print('строка состоит только из символов')

# 6
id = 49001011111

pattern = re.compile(r'[1-8][0-9][0-9]#########')  # not sure, sorry

matches = pattern.finditer(id)

for match in matches:
    print(match)



