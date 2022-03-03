def hello_func():
    pass


print(hello_func)  # <function hello_func at 0x000001B3287A6948>
print(hello_func())  # None

def hello_func(greeting, name = 'You'):
    return '{} {}'.format(greeting, name)


print(hello_func('Hi'))  # Hi You, with default argument provided
print(hello_func('Hello', 'Harsh'))  # Hello Harsh

def student_info(*args, **kwargs):
    print(args)  # ('Math', 'Art')  # Tuple of items
    print(kwargs)  # {'name': 'John', 'age': 22}



student_info('Math', 'Art', name='John', age=22)

def student_info1(*args, **kwargs):
    print(args)  # (['Math', 'Art'], {'name': 'John', 'age': 22})  no unpacking done here
    print(kwargs)  # {}

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info1(courses, info)

def student_info2(*args, **kwargs):
    print(args)  # ('Math', 'Art')
    print(kwargs)  # {'name': 'John', 'age': 22}


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info2(*courses, **info)  # putting * and ** do unpacking of values

# Leap year
# Number of days per month.First value placeholder for indexing purpose
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    '''
    :param year:
    :return: True for leap years and False for non-leap year
    '''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    '''
    :param year:
    :param month:
    :return: number of days in that month in that year
    '''

    if not 1 <= month <= 12:
        return 'Invalid month'

    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


print(is_leap(2017))  # False
print(is_leap(2020))  # True
print(days_in_month(2017, 2))  # 28
print(days_in_month(2020, 2))  # 29
print(days_in_month(2020, 12))  # 31
