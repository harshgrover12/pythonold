# List is mutable

courses = ['history', 'math', 'physics', 'compsci']
print(courses)
print(len(courses))  # 4
print(courses[-1])   # compsci
print(courses[0:2])  # ['history', 'math']
print(courses[2:])   # ['physics', 'compsci']
courses.append('Art')
print(courses)    # ['history', 'math', 'physics', 'compsci', 'Art']
courses.insert(1, 'chemistry')
print(courses)   # ['history', 'chemistry', 'math', 'physics', 'compsci', 'Art']
courses_2 = ['Bio', 'Pharma']
courses.insert(0, courses_2)
print(courses)  # [['Bio', 'Pharma'], 'history', 'chemistry', 'math', 'physics', 'compsci', 'Art']

# extend will add items at the end each individual item but append will add item as list.
courses.extend(courses_2)
print(courses)   # [['Bio', 'Pharma'], 'history', 'chemistry', 'math', 'physics', 'compsci', 'Art', 'Bio', 'Pharma']

# append list
courses.append(courses_2)
print(courses)  #  [['Bio', 'Pharma'], 'history', 'chemistry', 'math', 'physics', 'compsci', 'Art', 'Bio', 'Pharma', ['Bio', 'Pharma']]


courses.remove('math')
print(courses)  # [['Bio', 'Pharma'], 'history', 'chemistry', 'physics', 'compsci', 'Art', 'Bio', 'Pharma', ['Bio', 'Pharma']]

courses.pop()  # if no number passed as argument to pop, it will pop out last item of list by default
print(courses)  # [['Bio', 'Pharma'], 'history', 'chemistry', 'physics', 'compsci', 'Art', 'Bio', 'Pharma']

courses.reverse()
print(courses)  # ['Pharma', 'Bio', 'Art', 'compsci', 'physics', 'chemistry', 'history', ['Bio', 'Pharma']]

courses.pop()  # sort is not possible between string and list element so popping out last element.
print(courses)

courses.sort()
print(courses)  # ['Art', 'Bio', 'Pharma', 'chemistry', 'compsci', 'history', 'physics']

courses.sort(reverse=True)
print(courses)  # ['physics', 'history', 'compsci', 'chemistry', 'Pharma', 'Bio', 'Art']

# if we want to sort list without altering original list then we use sorted function
# we need to assign sorted value in another list for it to work
nums = [1, 5, 2, 4, 3]
sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 2, 3, 4, 5]
print(nums)  # [1, 5, 2, 4, 3]

print(min(nums))  # 1
print(max(nums))  # 5
print(sum(nums))  # 15

print(courses.index('compsci'))  # 2
print('Art' in courses)  # True
print('math' in courses)  # False

for course in enumerate(courses):
    print(course, end='')  #  (0, 'physics')(1, 'history')(2, 'compsci')(3, 'chemistry')(4, 'Pharma')(5, 'Bio')(6, 'Art')

 # for index, course in enumerate(courses, start = 1) -- this will start from 1st element in the list.
 # (1, 'history')(2, 'compsci')(3, 'chemistry')(4, 'Pharma')(5, 'Bio')(6, 'Art')
print()
courses_str = ','.join(courses)
print(courses_str)  # physics,history,compsci,chemistry,Pharma,Bio,Art
print(type(courses_str))  # <class 'str'>

new_list = courses_str.split(',')
print(new_list)  # ['physics', 'history', 'compsci', 'chemistry', 'Pharma', 'Bio', 'Art']
