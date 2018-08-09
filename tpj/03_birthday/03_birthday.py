"""
The app takes a date and then compares it with today and tells you how many days
to your birthday
"""


import datetime

print('-----------------------------------------------')
print('                 Birthday App')
print('-----------------------------------------------')
print()

year=int(input('What year were you born [YYYY]? '))
month=int(input('What month were you born [MM]? '))
day=int(input('What day were you born [DD]? '))

birthday = datetime.date(year, month, day)
now = datetime.date.today()
bday_current_year = datetime.date(year=now.year, month=birthday.month,
                                  day=birthday.day)

days_to_birthday = bday_current_year - now 

if days_to_birthday.days < 0:
    print(f'You had your birthday {days_to_birthday.days} days ago')
elif days_to_birthday.days > 0:
    print(f'{days_to_birthday.days} days to go!')
else:
    print(f'Happy Birthday!')
