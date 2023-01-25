# 1
# year
current_year = 2023
year_of_birth = 1988
print(current_year-year_of_birth)
age = (current_year-year_of_birth)

# 2
# code parts
code_1 = '354'
code_3 = 132
# code 2 data
x = 152
y = 132
print(int(((x % y) * 13)**0.5))
code_2 = (int(((x % y) * 13)**0.5))   # make integer to round DOWN

# 3
code_1 = int(code_1)
print(str(code_1) + '-' + str(code_2) + '-' + str(code_3))
code_final = (str(code_1) + '-' + str(code_2) + '-' + str(code_3))

# 4
# name
user_name = 'John'
user_surname = 'Smith'
print('Hello ' + str(user_name) + ' ' + str(user_surname) + '. Your age is ' +
      str(age) + ' years old. Your secret code is ' + str(code_final) + '.')
