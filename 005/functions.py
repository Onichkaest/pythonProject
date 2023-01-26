import funcs

print(funcs.double(4))  # 8


from funcs import double
print(double(5))  # 10

from funcs import double as dbl
print(dbl(123))  # 246