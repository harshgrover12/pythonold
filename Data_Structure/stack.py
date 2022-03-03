# s = list()
# s.append('https://www.cnn.com/')
# s.append('https://www.cnn.com/world')
# s.append('https://www.cnn.com/india')
# s.append('https://www.cnn.com/china')
#
# print(s.pop())
# print(s)
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s)

'''
https://www.cnn.com/china
['https://www.cnn.com/', 'https://www.cnn.com/world', 'https://www.cnn.com/india']
https://www.cnn.com/india
https://www.cnn.com/world
https://www.cnn.com/
Traceback (most recent call last):
  File "C:/D-Drive/learning/Corey-Schafer/Data_Structure/stack.py", line 12, in <module>
    print(s.pop())
IndexError: pop from empty list
'''

# list can not be used as stack, problem is it has to allocate new memory everytime.
# recommended approach is to use collections.deque

from collections import deque

stack = deque()
stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
stack.append('https://www.cnn.com/china')
# print(stack)  # deque(['https://www.cnn.com/', 'https://www.cnn.com/world', 'https://www.cnn.com/india', 'https://www.cnn.com/china'])
stack.pop()
# print(stack)  # deque(['https://www.cnn.com/', 'https://www.cnn.com/world', 'https://www.cnn.com/india'])


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


# s = Stack()
# s.push(5)
# print(s.peek())  # 5
# print(s.is_empty())  # False
# print(s.size())  # 1

