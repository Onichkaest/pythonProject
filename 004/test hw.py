while True:  # will continue forever
    try:
        user_id = input('Please enter ID code: ')
        int(user_id)  # convert to integer       if not number and cannot convert to integer, ValueError and will print to enter numeric
        if len(user_id) != 11:   #!=not equal.  If length is not 11 will trigger Exception
            raise Exception
    except ValueError:  # if cannot be converted to integer
        print('Code you entered is not numeric.')
        continue  # will go back to enter ID
    except Exception:
        if len(user_id) > 11:
            print('Code is too long!')
        else:
            print('Code is too short!')
        continue
    else:
        print('Your ID code is', user_id)
        break
gender = int(user_id[0])    #1 for man 1800-1899, 2 for woman 1800-1899, 3 for man 1900 to 1999, 4 for woman 1900 to 1999, 5 for 2000 to 2099, 6 for woman 2000 to 2099
year_of_birth = int(user_id[1:3])
month_of_birth = int(user_id[3:5])
date_of_birth = int(user_id[5:7])
hospital_of_birth = int(user_id[7:10])
control = int(user_id[-1])



while True:  # will continue forever
    try:
        user_id = input('Please enter ID code: ')
        int(user_id)  # convert to integer       if not number and cannot convert to integer, ValueError and will print to enter numeric
        if len(user_id) != 11:   #!=not equal.  If length is not 11 will trigger Exception
            raise Exception
    except ValueError:  # if cannot be converted to integer
        print('Code you entered is not numeric.')
        continue  # will go back to enter ID
    except Exception:
        if len(user_id) > 11:
            print('Code is too long!')
        if len(user_id) < 11:
            print('Code is too short!')
        continue
gender = int(user_id[0])
while True:
    try:
        if gender > 6:
            raise Exception
    except Exception:
        if gender > 6:
            print ('code invalid')
        continue

#1 for man 1800-1899, 2 for woman 1800-1899, 3 for man 1900 to 1999, 4 for woman 1900 to 1999, 5 for 2000 to 2099, 6 for woman 2000 to 2099
year_of_birth = int(user_id[1:3])
month_of_birth = int(user_id[3:5])
date_of_birth = int(user_id[5:7])
hospital_of_birth = int(user_id[7:10])
control = int(user_id[-1])
