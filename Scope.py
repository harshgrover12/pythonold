"""
LEGB
Local, Enclosing, Global, Built-in
"""

x = 'global x'

def test():
    y = 'local y'
    print(y)   # local y
    print(x)   # global x, as x is not defined in local scope so it looks out in enclosing scope
               # then it check in global scope and here variable is existing

test()
# print(y)  # name 'y' is not defined

def test():
    x = 'local x'  # here x is not overridden defined outside function
    print(x)  #  local x

test()
print(x)  # global x

def test():
    global x
    x = 'local x' # here x variable defined in global scope will be overridden
    print(x)  # local x

test()
print(x)  # local x

def test(z):
    print(z)

test('local z')

# Built-in

def min():
    pass

# m = min([5,4,3,2,1])
# print(m)  # min() takes 0 positional arguments but 1 was given, here it is
# giving priority to function defined in global scope instead of built-in min function.

# Enclosing

def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x)  # Here inner x will be printed as there is variable defined inside inner fun
    inner()
    print(x)  #  Here variable defined in outer function will be printed which is local to outer function
outer()

# If x defined inside inner function is commented then outer x will be printed both the times
# as it looks for variable in enclosing scope after checking in local scope.
# now if x is uncommented back in inner funcion and x is commnened inside outer function then
# error will be thrown for second print as x is not found in local scope of outer function.

'''if we want to modify variable defined inside enclosing function then below code can be used'''

# nonlocal
def outer():
    x = 'outer x'
    def inner():
        nonlocal x
        x = 'inner x'
        print(x)  #  inner x
    inner()
    print(x)  # inner x
outer()
print(x)  # local x