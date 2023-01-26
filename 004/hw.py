id_code = input('Please enter your national id: ')
if len(id_code) == 11:
    print('Your ID code is', id_code)
elif len(id_code) > 11:
    print('Code you entered is longer than 11 digits')
else:
    print('Code you entered is shorter than 11 digits')


try:
    user_input = float(input('Enter number:'))
except:
    print('Must enter a number!')  # if not float
else:
    print(user_input ** 2)  # if there is no mistake will do **
finally:
    print('Good bye!')  # will always print

while True:  # will continue forever
    try:
        user_id = input('Please enter ID code: ')
        int(user_id)
    except:
        print('Code you entered is not numeric.')
        continue
    else:
        print('Your ID code is', user_id)
        break


while True:  # will continue forever
    try:
        user_id = input('Please enter ID code: ')
        int(user_id)  # convert to integer
        if len(user_id) != 11:
            raise Exception
    except ValueError:  # if cannot be converted to integer (letters)
        print('Code you entered is not numeric.')
        continue
    except Exception:
        if len(user_id) > 11:
            print('Code is too long!')
        else:
            print('Code is too short!')
        continue
    else:
        print('Your ID code is', user_id)
        break
