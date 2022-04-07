from ast import If
from datetime import date
import calendar
curr_date = date.today()
print(calendar.day_name[curr_date.weekday()])

If (curr_date = calendar.SUNDAY or calendar.SATURDAY)
print('today is the weekend, Yessir')


