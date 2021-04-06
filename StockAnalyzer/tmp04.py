from datetime import datetime
import calendar

tmnow = datetime.now()
lastDay = calendar.monthrange(tmnow.year, tmnow.month)
print(calendar.calendar(2021))
print(lastDay)
print(calendar.monthrange(2021, 4))