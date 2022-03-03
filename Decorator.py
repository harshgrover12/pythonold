# Function to be decorated will be passed as argument to decorator_function and wrapper_function
# will return the decorate function(original_function given to decorator for decoration)
from functools import wraps


def decorator_func(original_func):
    def wrapper_func():
        print('wrapper executed this before {}'.format(original_func.__name__))
        return original_func()
    return wrapper_func


@decorator_func
def display():
    print('original function ran')

display()


# decorated_display = decorator_func(display)
# decorated_display()

'''
o/p
wrapper executed this before display
original function ran

decorator_func is called with original function passed as argument which is returning
wrapper_func and wrapper_func internally returning original_func functionality.

decorated_display = decorator_func(display)
decorated_display()
above two lines can be replaced by writing @decorator_function on top of display()
and then display() function can be run.
'''

'''
If we want to use decorator function to decorate two or more function at the same time then
we need to pass *args, **kwargs in the wrapper function
without adding those we will be getting below error:
wrapper_function() takes 0 positional arguments but 2 were given
'''


def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_func


@decorator_func
def display():
    print('original function ran')


display()


@decorator_func
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)

'''
output:
wrapper executed this before display
original function ran
wrapper executed this before display_info
display_info ran with arguments (John, 25)
'''

# Decorator functionality can be achieved using class as well

# class decorator_class(object):
#
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print('call method executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args, **kwargs)
#
# @decorator_func
# def display():
#     print('original function ran')
#
# display()
#
# @decorator_func
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))


#output is same as before done with function

# Decorators practical examples
# example-1, logging functionality decorator can be applied to any function and we don't have
# to rewrite logging functionality for all the functions

def my_logger(original_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.INFO)

    @wraps(display_info)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return original_func(*args, **kwargs)
    return wrapper


@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)

# example-2


def timer(orig_func):
    import time

    @wraps(display_info)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper

import time

@my_logger
@timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Harsh', 34)

# display_info ran in : 1.0076963901519775 sec

# applying multiple decorators to one function

'''
@my_logger
@timer
is equal to
display_info = my_logger(my_timer(display_info))
lower function will be called first(nearer to the function in stack)
It will create problem for the outer function as wrapper of inner function will be passed
to avoid this problem, we need to import "from functools import wraps"
and then wrapper functions..we need to put decorator like below:

@wraps(orig_func)
def wrapper(*args, **kwargs)

'''