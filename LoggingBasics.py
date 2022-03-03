import logging
'''
DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or indicative of some problem
in the near future(e.g Disk space low). The software is working as expected.
ERROR: Due to a more serious problem, the software has been able to perform some function.
CRITICAL: A serious error, indicating that program itself may be able to continue running.
'''

# By default, it will log warning, error and critical

logging.basicConfig(filename='logging.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def add(a, b):
    return a+b


num1 = 10
num2 = 5
add_result = add(num1, num2)
logging.debug('Add: {} + {} = {}'.format(num1, num2, add_result))  # Nothing returned as default is warning plus
# Above line will be printed on console once logging.basicConfig(level=logging.DEBUG) is added.
logging.warning('Add: {} + {} = {}'.format(num1, num2, add_result))  # WARNING:root:Add: 10 + 5 = 15
