# Tuple is immutable
# we use parenthesis instead of square bracket in tuple
tuple_1 = ('History', 'Math', 'Physics', 'Compsci', 'Physics', {'chemistry', 'english'}, ['Compsci', 'Math'])
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'
# print(tuple_1)
# print(tuple_2)

'''
 tuple_1[0] = 'Art'
TypeError: 'tuple' object does not support item assignment
'''

print(tuple_1.index('Math'))  # 1
print(tuple_2.count('Physics')) # 2
tuple_2[-1][0] = 'Science'
print(tuple_2)  # ('History', 'Math', 'Physics', 'Compsci', 'Physics', ['Science', 'Math'])
tuple_2[-2][0] = 'Hindi'
print(tuple_2)  # 'set' object does not support item assignment

# If mutable element is present in the tuple, then it can be changed