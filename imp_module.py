from my_module import find_index, test
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index('math', courses)
print(index)
print(test)
print(sys.path)
# python look for module in directories mentioned in sys.path in the order items in the list are shown
# if module is not found where the script is then we can use sys.path.append and append the path
sys.path.append('path of the module')
# other option is to add entry in environment variable, it will be next to current directory in the list.
# export PYTHONPATH="MODULE_PATH"
# after adding path in  environment then module will be like generic module and can be imported from anywhere.
# if module is not in current script and in PYTHONPATH, then it looks for module in standard python lib.

import calendar
print(calendar.isleap(2020))  # True

import os
print(os.__file__)

