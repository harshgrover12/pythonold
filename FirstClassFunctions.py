'''
First Class Function:
A Programming language is said to have first class function if it treats functions as first-class citizens

First Class Citizen (Programming)
A first class citizen(objects) is an entity which supports all the operations generally available to
other entities. These operations typically include being:
passed as an argument
returned from a function
Assigned to a variable
'''

# Function assigned to a variable
def square(x):
    return x*x

f = square
print(f)  # <function square at 0x000001FE301A5948>
print(square)  # <function square at 0x000001FE301A5948>
print(f(5))  # 25, it is working same like square(5) as now function is assigned to f variable

# Function as an argument
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

square = my_map(square, [1,2,3,4,5])  # square is not passed with paranthesis
print(square)  # [1, 4, 9, 16, 25]

def cube(x):
    return x*x*x

cube = my_map(cube, [1,2,3,4,5])  # cube is added as argument but not as a function
print(cube)  # [1, 8, 27, 64, 125]

# function returned from another function

def logger(msg):
    def log_msg():
        print('Log:', msg)
    return log_msg

log_hi = logger('Hi')
log_hi()

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text

print_h1 = html_tag('h1')  # html_tag function is called here and value of which is assigned to print_h1
print(print_h1.__name__)  # output = wrap_text, print_h1 value is equal to inner function
# as that is what returned from html_tag function
print_h1('Test Headline!')  # <h1>Test Headline!</h1>, value of print_h1 is remembered and used
print_h1('Another headline!') # <h1>Another headline!</h1>, value of print_h1 is remembered and used