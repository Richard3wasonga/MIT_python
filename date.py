import datetime
import pytz

# Naive
# tday = datetime.date.today()
# print(tday.weekday())
# print(tday.isoweekday())

# tdelta = datetime.timedelta(days=7)

# print(tday + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

# bday = datetime.date(2026, 9, 24)

# till_bday = bday - tday
# print(till_bday.days)
# print(till_bday.total_seconds())

# t = datetime.time(9, 30, 45, 100000)
# print(t.hour)

# dt = datetime.datetime(2026, 7, 26, 12, 30, 45, 100000)

# tdelta = datetime.timedelta(hours=12)

# print(dt + tdelta)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt = datetime.datetime(2026, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)


# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

# dt_eat = dt_utcnow.astimezone(pytz.timezone('Africa/Nairobi'))
# print(dt_eat)

# dt_eat = datetime.datetime.now()
# nk_tz = pytz.timezone('Africa/Nairobi')

# dt_eat = nk_tz.localize(dt_eat)

# print(dt_eat)

# dt_td = dt_eat.astimezone(pytz.timezone('Africa/Dar_es_Salaam'))
# print(dt_td)


dt_eat = datetime.datetime.now(tz=pytz.timezone('Africa/Nairobi'))

print(dt_eat.isoformat())
print(dt_eat.strftime('%B %d %Y'))

# converting string into datetime
# have to pass in the string and the format it is in as refrenced from python documentation
dt_str = 'May 17 2026'

dt = datetime.datetime.strptime(dt_str, '%B %d %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime

# for tz in pytz.all_timezones:
#     print(tz)