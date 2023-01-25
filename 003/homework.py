for num1 in range(0,101):
    if num1 % 15 == 0:  # if num1 % 5 == 0 and num1 % 3 == 0:
        print(num1, "FizzBuzz")
    elif num1 % 3 == 0:
        print(num1, "Fizz")
    elif num1 % 5 == 0:
        print(num1, "Buzz")


