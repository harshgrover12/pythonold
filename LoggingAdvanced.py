import logging
import EmployeeForLogging

'''
On importing EmployeeForLogging, employee.log there will be logs printed but sample.log is not generated
Root logger will be setup seeing EmployeeForLogging class as that is imported before setting up basicconfig
in this class
We need to create new logger to solve this problem.
'''

# By default, it will log warning, error and critical
# its not good practice to work with root logger

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)  # logging level can be set at file handler level
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()  # This will print error/result at console also.
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(a, b):
    return a+b


def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        logger.exception('Tried divide by zero')
    else:
        return result


num1 = 10
num2 = 0
add_result = add(num1, num2)
divide_result = divide(num1, num2)
# we need to use logger now instead of logging which is root level
logger.debug('Add: {} + {} = {}'.format(num1, num2, add_result))  # Nothing returned as default is warning plus
logger.debug('Divide: {} / {} = {}'.format(num1, num2, divide_result))
'''
DEBUG:__main__:Add: 10 + 5 = 15, not using root logger now
'''
'''
on setting error level to error at file handler level below logs will be printed
ERROR:__main__:Tried divide by zero
Traceback (most recent call last):
  File "C:/D-Drive/learning/Corey-Schafer/LoggingAdvanced.py", line 32, in divide
    result = a/b
ZeroDivisionError: division by zero

'''