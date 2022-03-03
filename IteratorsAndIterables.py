# If something is iterable then it will have special method __iter__() implemented
nums = [1,2,3]
print('__iter__' and '__next__' in dir(nums))  # False, as __next__ is not present, still list is not iterator
# We can loop over the item(list,tuple etc) if it has __iter__ method
# List is iterable but it is not Iterator.
# Iterator is an object with the state which remembers the state where it is during iteration.
# List doesn't have next() method in dir(list)
# print(next(nums))
'''
Traceback (most recent call last):
  File "C:/D-Drive/learning/Corey-Schafer/IteratorsAndIterables.py", line 8, in <module>
    print(next(nums))
TypeError: 'list' object is not an iterator
'''
# i_nums = nums.__iter__()
i_nums = iter(nums)
print(i_nums) # <list_iterator object at 0x000001884C9547C8>
print('__iter__' and '__next__' in dir(i_nums))  # True, as now both __iter__ and __next__
# is present after converting it to iterator
print(next(i_nums))  # 1, as i_nums is iterator
print(next(i_nums))  # 2, as it remembered previous state and that is the property of iterator
print(next(i_nums))  # 3
# print(next(i_nums))  # StopIteration as it has run out of elements
'''
Traceback (most recent call last):
  File "C:/D-Drive/learning/Corey-Schafer/IteratorsAndIterables.py", line 23, in <module>
    print(next(i_nums))
StopIteration
'''
# For loop takes care of StopIteration exception which is implemented like below in background
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break
'''
1
2
3
'''
# with next we can only go forward and not backward


class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self  # it returns the object itself

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)
print(type(nums))  # <class '__main__.MyRange'>

for num in nums:
    print(num)

'''
1
2
3
1
2
3
4
5
6
7
8
9
'''


def my_range(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


nums1 = my_range(1, 5)
print(nums1)  # <generator object my_range at 0x000001A5E28FD3C8>
print(next(nums1)) # 1
print(next(nums1)) # 2
print(next(nums1)) # 3
print(next(nums1)) # 4
print(next(nums1)) # 5


