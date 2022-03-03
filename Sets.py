# set, we use curly braces to place items
cs_courses = {'History', 'Math', 'Physics', 'Compsci', 'Math'}
print(cs_courses)  # {'Compsci', 'History', 'Physics', 'Math'}
print('Math' in cs_courses)  # True
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))  #  {'Math', 'History'} common in both sets
print(cs_courses.difference(art_courses))  # {'Compsci', 'Physics'} to see which courses in cs_course but not in art_courses
print(cs_courses.union(art_courses))  #  {'Design', 'Compsci', 'Math', 'Art', 'Physics', 'History'}

# Empty list
empty_list = []
empty_list = list()

# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty set
empty_set = {} # This is not right, its an dict
empty_set = set()