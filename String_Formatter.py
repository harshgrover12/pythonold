import datetime
person = {'name': 'john', 'age': 23}
sentence = 'My name is {name} and age is {age}'.format(**person)
print(sentence)  # My name is john and age is 23

# ** do dictionary unpacking

pi = 3.14159265
print('Pi is equal to {:.2f}'.format(pi))  # 3.14, printed upto 2 decimal places

print('1 Mb is equal to {:,} bytes'.format(1000**2))  # 1 Mb is equal to 1,000,000 bytes
print('1 Mb is equal to {:,.2f} bytes'.format(1000**2)) # 1 Mb is equal to 1,000,000.00 bytes

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
sentence1 = '{:%B %d, %Y}'.format(my_date)
print(sentence1)  # September 24, 2016

