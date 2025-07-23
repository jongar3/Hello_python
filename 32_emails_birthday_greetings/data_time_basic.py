import datetime as dt

now= dt.datetime.now() #(.now is a match)
print(now)
week_day = now.weekday()  # Monday is 0, Sunday is 6
print(week_day)
print(now.month)

birth_date = dt.datetime(year=2004, month=7, day=19)
print(birth_date)