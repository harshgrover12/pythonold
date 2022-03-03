if True:
    print('Conditional was true')

language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

# Python doesn't have switch case statement

user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad creds')

user = 'Admin'
logged_in = True
if not logged_in:
    print('Login to Admin page')
else:
    print('Welcome!')

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)  # False, as both are two different objects in the memory
print(id(a))  # 1437418869256
print(id(b))  # 1437418869768

a = [1, 2, 3]
b = a
print(id(a))  # 2318532921480
print(id(b))  # 2318532921480
print(a is b)  # True
print(a == b)  # True

# False, None, 0 evaluates to False
# Empty sequence, '', [], (), {} - evaluates to False
