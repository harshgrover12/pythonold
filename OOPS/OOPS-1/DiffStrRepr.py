import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

b = str(a)

print('str(a): {}'.format(str(a)))  # str(a): 2022-01-22 18:04:47.672839+00:00
print('str(b): {}'.format(str(b)))  # str(b): 2022-01-22 18:04:47.672839+00:00

print()

print('repr(a): {}'.format(repr(a)))  # repr(a): datetime.datetime(2022, 1, 22, 18, 4, 47, 672839, tzinfo=<UTC>)
print('repr(b): {}'.format(repr(b)))  # repr(b): '2022-01-22 18:04:47.672839+00:00'

# str representation is clear but repr representation is unambigious