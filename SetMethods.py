s1 = set([1,2,3,4,5,1,2,3])
print(s1)  # {1, 2, 3, 4, 5}
s1.add(6)
print(s1)  # {1, 2, 3, 4, 5, 6}
s2 = {7,8,9}
s1.update([6,7,8],s2)
print(s1)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
s1.remove(5)
print(s1) # {1, 2, 3, 4, 6, 7, 8, 9}

# Difference between remove and discard, remove throws keyerror and discard do not

s1.discard(5)
print(s1)  # {1, 2, 3, 4, 6, 7, 8, 9}

# s1.remove(5)
# print(s1)
'''
Traceback (most recent call last):
  File "C:/D-Drive/learning/Corey-Schafer/SetMethods.py", line 10, in <module>
    s1.remove(5)
KeyError: 5
'''
s1.discard(5)
print(s1)

set1 = {1,2,3}
set2 = {2,3,4}
set3 = {3,4,5}

# common elements between two sets
set4 = set1.intersection(set2)
print(set4) # {2, 3}

set5 = set1.intersection(set2, set3)
print(set5)  # {3}

# Items which are different, item present in set1 but not in set2
set6 = set1.difference(set2)
print(set6)  # {1}, 1 is unique element in set1 which is not present in set2,
# 4 is not returned as difference is run on set1 and not on set2

set7 = set2.difference(set1)
print(set7)  # {4}

set8 = set2.difference(set1, set3)
print(set8)  # set(), empty set as 2,3 is present in set1 and 4 is present in set3 so no unique element.

set9 = set3.difference(set1,set2)
print(set9)  # {5}

# to find all the unique values in 2 sets we can use symmetric_difference method.
set10 = set1.symmetric_difference(set2)
set11 = set2.symmetric_difference(set1)
print(set10)  # {1,4}, it is giving all the unique elements unlike difference method.
print(set11)  # {1, 4}

l1 = [1,2,3,1,2,3]
print(list(set(l1)))  # [1, 2, 3]

employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
gym_members = ['April', 'John', 'Corey']
developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

result = set(gym_members).intersection((developers))  # first list need to be casted as intersection method applies
# to set only and second list is not required to be casted.
print(result)  # {'Corey', 'April'}

result1 = set(employees).difference(gym_members, developers)
print(result1)  # {'Jenn', 'Jim'}

# Doing membership test on sets provides better performance than list if list is very big.
if 'Corey' in developers:
    print('found!')

