import datetime

##################datetime.date###################
d = datetime.date(2016, 7, 24)
print(d)  #  2016-07-24

tday = datetime.date.today()
print(tday)  # 2022-01-15

tday_day = datetime.date.today()
print(tday_day.day)  # 15
print(tday.isoweekday())  # 6 monday=0, sunday is 7
print(tday.weekday())  # 5   monday=1, sunday is 6

# timedelta
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)  # 2022-01-22
print(tday-tdelta)  # 2022-01-08

bday = datetime.date(2022, 3, 12)
till_bday = bday-tday
print(till_bday)  # 56 days for to be 35


#########datetime.time#################

t = datetime.time(9, 30, 55, 100000)
print(t)  # 09:30:55.100000

############datetime.datetime##########

dt = datetime.datetime(2022, 3, 12, 9, 30, 55, 100000)
print(dt)  # 2022-03-12 09:30:55.100000
print(dt.date())   # 2022-03-12
print(dt.time())  # 09:30:55.100000
tdelta1 = datetime.timedelta(hours=12)
print(dt+tdelta1)  #  2022-03-12 21:30:55.100000

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)  # 2022-01-15 16:05:03.557458  # current local time with timezone=None
print(dt_now)  # 2022-01-15 16:05:03.557458  # Here we can pass timezone info
print(dt_utcnow)  # 2022-01-15 10:35:03.557458  # current utc time with timezone=None

################pytz#################

import pytz

# timezone aware time using utc

dt1 = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt1)  # 2016-07-27 12:30:45+00:00, +00:00-UTC offset

dt_utcnow1 = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow1)  # 2022-01-15 10:55:34.078639+00:00

dt_ind = dt.utcnow().astimezone(pytz.timezone('Asia/Calcutta'))
print(dt_ind)  # 2022-01-15 11:01:03.998187+05:30 , +05:30 is timezone difference

# for tz in pytz.all_timezones:
#     print(tz)

# naive time to timezone aware

lcl_time = datetime.datetime.now()
print(lcl_time)  # 2022-01-15 11:06:28.675219+05:30
ind_tz = pytz.timezone('Asia/Calcutta')
lcl_time = ind_tz.localize(lcl_time)  # 2022-01-15 16:36:28.906186


############################    datetime to string      ####################################
# strftime- Datetime to string
dt_calcutta = datetime.datetime.now(tz=pytz.timezone('Asia/Calcutta'))
print(dt_calcutta.strftime('%B %d, %Y'))  # January 15, 2022

########################## string to datetime #########################
# strptime - String to Datetime
dt_str = 'January 15, 2022'
dt12 = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt12)  # 2022-01-15 00:00:00