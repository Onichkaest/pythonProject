import datetime

# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
new_date = datetime.datetime.strptime(sample1, '%b %d %Y %H:%M%p')
print(new_date)
sample2 = '14:20 10/12/22'  # YY/MM/DD
new_date2 = datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d')
print(new_date2)
sample3 = 'Tuesday, September 24, 2019'
new_date3 = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
print(new_date3)
sample4 = '01.01.1970 - 00:00:01'
new_date4 = datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
print(new_date4)

# Write a program to print yesterdays, today and tomorrow dates
#yesterday
print(datetime.date.today()-datetime.timedelta(days=1))
#today
print(datetime.date.today())
#tomorrow
print(datetime.date.today()+datetime.timedelta(days=1))

# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
dayday = datetime.datetime.fromtimestamp(1014163200)
print(dayday.strftime('%d.%m.%Y'))

# Write a function to subtract 2 weeks from timestamp and return new timestamp
daydayday = dayday-datetime.timedelta(weeks=2)
print(daydayday.timestamp())
