while True:
    try:
        user_input = input('Please enter your Estonian national ID number: ')
        user_input = str(int(user_input))
        print(user_input)
        if len(user_input) != 11:
            raise UserWarning

    except ValueError:
        print('Code you entered is not numeric')
        continue
    except UserWarning:
        print('Code you entered is not 11 numbers long')
        continue
    else:
        print('Else statement')
    finally:
        print('Program finished working')
gender = int(user_id[0])
year_of_birth = int(user_id[1:3])
month_of_birth = int(user_id[3:5])
date_of_birth = int(user_id[5:7])
hospital_of_birth = int(user_id[7:10])
control = int(user_id[-1])
