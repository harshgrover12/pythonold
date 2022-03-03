message = 'Hello World'
print(len(message))
print(message[0])
print(message[0:5])  # Hello
print(message[:5])  # Hello
print(message[6:])  # World
print(message.lower())  # hello world
print(message.upper())  # HELLO WORLD
print(message.count('Hello'))   # 1
print(message.count('l'))     # 3
print(message.find('w'))   # returns -1 if not found in the string
print(message.find('W'))   # 6
print(message.find('l'))   # 2, first match in the string
message.replace('World', 'India')
print(message)  # this will print Hello World as replaced string is not assigned to message variable
new_msg = message.replace('World', 'Universe')
print(new_msg)  # Hello Universe
print(message.replace('World', 'India'))  # Hello India

greeting = 'Hello'
name = 'Michael'
greet_msg = greeting + ' ' + name
print(greet_msg)
greet_msg = '{} {}, how are you'.format(greeting, name)
print(greet_msg)
greet_msg = f'{greeting} {name.upper()}, how are you'
print(greet_msg)
print(help(str.lower))


