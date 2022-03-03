nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# i want n for each item in n normal way
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# comprehension way
print([n for n in nums])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#n*n comprehension
print([n*n for n in nums])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# using map
my_list1 = map(lambda n:n*n, my_list)
print(list(my_list1))  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# even number using comprehension
print([n for n in nums if n % 2 == 0])  # [2, 4, 6, 8, 10]

# using filter
my_list2 = filter(lambda n:n%2==0, my_list)
print(list(my_list2))  # [2, 4, 6, 8, 10]

# pair of letter and number using normal way
list1 = []
for letter in 'abcd':
    for num in range(4):
        list1.append((letter, num))
print(list1)  # [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0),
# ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]

# comprehension way
print([(letter, num) for letter in 'abcd' for num in range(4)])


# Dictionary comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverline', 'Deadpool']
print(list(zip(names)))  # [('Bruce',), ('Clark',), ('Peter',), ('Logan',), ('Wade',)]
print(list(zip(names, heroes)))  # [('Bruce', 'Batman'), ('Clark', 'Superman'), ('Peter', 'Spiderman'),
# ('Logan', 'Wolverline'), ('Wade', 'Deadpool')]

my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero
print(my_dict)  # {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverline', 'Wade': 'Deadpool'}

# comprehension way
my_dict1 = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(my_dict1)  # {'Bruce': 'Batman', 'Clark': 'Superman', 'Logan': 'Wolverline', 'Wade': 'Deadpool'}

# Set Comprehension

# List to set
numbers = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in numbers:
    my_set.add(n)
print(my_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print({n for n in numbers})  # {1, 2, 3, 4, 5, 6, 7, 8, 9}


# Generator expression
def gen_func(nums):
    for n in nums:
        yield n*n


my_gen = gen_func(nums)
for n in my_gen:
    print(n)

# Generator comprehension, we use parenthesis to enclose
my_gen1 = (n*n for n in nums)
for i in my_gen1:
    print(i)