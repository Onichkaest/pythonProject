empty_dict = {}
print(type(empty_dict))  # <class 'dict'>
empty_dict = {'name': 'Roman', 'surname': 'Roman'}  # cannot have duplicate. but
empty_dict = {'name': 'Roman', 'surname': 'Kutselepa', 1: 'One'}
x = 5
empty_dict = {'name': 'Roman', 'surname': 'Kutselepa', 1: 'One', x: 'Five'}
print(empty_dict)  # {'name': 'Roman', 'surname': 'Kutselepa', 1: 'One', 5: 'Five'}
print(empty_dict['name'])  # Roman
empty_dict = {'name': 'Roman', 'surname': 'Kutselepa', 1: 'One', x: 'Five',
             'lst': [1, 2, 3, 4], 'dct': {'one': 1, 'two': 2}}
print(empty_dict['lst'])  # [1, 2, 3, 4]
print(empty_dict['lst'][0])  # 1
print(empty_dict['dct']['one'])
print(type(empty_dict['dct']))  # <class 'dict'>
print(empty_dict.get('job'))  # None   add .get to not get an error. safe method
print(empty_dict.get('job', 'False'))  # instead of None will be False... or anything else you specify

empty_dict = {'name': 'Roman', 'surname': 'Kutselepa', 1: 'One', x: 'Five',
             'lst': [1, 2, 3, 4], 'dct': {'one': 1, 'two': 2}}
empty_dict['name'] = 'Jack'
print(empty_dict)  # {'name': 'Jack', 'surname': 'Kutselepa', 1: 'One', 5: 'Five', 'lst': [1, 2, 3, 4], 'dct': {'one': 1, 'two': 2}}

empty_dict['phone'] = '555-555-555'
print(empty_dict)  # {'name': 'Jack', 'surname': 'Kutselepa', 1: 'One', 5: 'Five', 'lst': [1, 2, 3, 4], 'dct': {'one': 1, 'two': 2}, 'phone': '555-555-555'}
print(len(empty_dict))
empty_dict.update(name='Roman')
print(empty_dict)
empty_dict.update({'name': 'Jack', 'surname': 'Smith', 'job': 'Programmer'})
print(empty_dict)

x = empty_dict.pop('name')  # remembers and deletes
print(empty_dict)
print(x)
del empty_dict['surname']  # deletes
print(empty_dict)

print(empty_dict.keys())
print(empty_dict.values())
print(empty_dict.items())

for x in empty_dict.items():

    print(x[0])
    print(x[1])


