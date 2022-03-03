li = [9,1,8,2,7,3,6,4,5]
s_li = sorted(li)

print('sorted list:\t', s_li)
print('original list:\t', li)
# li.sort(), this will sort original list and returns None if variable sorted list is assigned.
# sorted function doesn't modify existing list else returns a new list

# Tuple doesn't have sort method so have to sorted function to sort the tuple
tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('Tuple\t', s_tup)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

di = {'name': 'corey', 'job':'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t', s_di)  # ['age', 'job', 'name', 'os'], returns key in sorted order

li1 = [-5, -6,-4,1,2,3]
s_li1 = sorted(li1)
print(s_li1)  # [-6, -5, -4, 1, 2, 3]

# sort with absolute value
s_li1 = sorted(li1, key=abs)
print(s_li1)  # [1, 2, 3, -4, -5, -6]