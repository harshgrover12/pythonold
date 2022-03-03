'''
A closure is inner function that remembers and has access to variables in the local scope
in which it was created even if outer function is done with execution.
'''

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}"  with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)  # 6
add_logger(4,5)  # 9

sub_logger(10, 5)  # 5
sub_logger(20, 10)  # 10


def outer_func(msg):
    message = msg

    def inner_func():
        print(message)
    return inner_func


hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()  # Hi, same like inner_func()
hello_func()  # Hello, same like inner_func()

