import datetime

t = datetime.time(5, 25, 1)
# and it prints time, which was printed earlier
print(t)
# we can specify and print hour for example
print(t.hour)

# show max date time in a day
print(datetime.time.max)

# receive today
today = datetime.date.today()
print(today)
# we can recieve more information
print(today.timetuple())
print(today.year)
