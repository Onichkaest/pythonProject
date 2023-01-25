# x = 10
# if x > 0:
#     print('X is a positive number')
#
#     print('Good bye!')

# x = -10
# if x > 0:
#     print('X is a positive number')
# elif x < 0:
#     print('X is a negative number')

x = -10
if x > 0:
    print('X is a positive number')
elif x < 0:
    print('X is a negative number')
else:
    print('X is zero')
print('Good bye!')

idcode = '49011111111'
if len(idcode) == 11:
    print('ID is valid')
else:
    if len(idcode) > 11:
        print('Code is too long')
    else:
        print('Code is too short!')

y = 10
if y > 0:
    print('Y is greater than 0')
elif y > 5:
    print('Y is greater than 5')
elif y > 9:
    print('Y is greater than 9')    # once first was true it did not check for others


