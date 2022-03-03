student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}
print(student['name'])  # John
# key can be numeric also but it should be unique

# Difference between get and student['key']
# if we try to get any value using a key which is not present in dictionary with below syntax then
# we get key error but if we use get function then returned value is None
# print(student[2])  # KeyError: 2
print(student.get(2))  # None
print(student.get(2, 'not found'))  # not found
student['phone'] = '55555-55555'  # adding new entry in dictionary
# {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci'], 'phone': '55555-55555'}
print(student)
student['name'] = 'Jane'  # Updating single item in dictionary
print(student)
# {'name': 'Jane', 'age': 25, 'courses': ['Math', 'Compsci'], 'phone': '55555-55555'}

# if we want to update multiple items in the dictionary then update function can be used
student.update({'name': 'Harsh', 'age': 3, 'courses': ['arts'], 'phone': '66666-66666'})
print(student)  # {'name': 'Harsh', 'age': 3, 'courses': ['arts'], 'phone': '66666-66666'}

del student['phone']
print(student)  # {'name': 'Harsh', 'age': 3, 'courses': ['arts']}

age = student.pop('age')
print(age)  # 3
print(student)  # {'name': 'Harsh', 'courses': ['arts']}

print(len(student))  # 2
print(student.keys())  # dict_keys(['name', 'courses'])
print(student.values()) # dict_values(['Harsh', ['arts']])
print(student.items())  # dict_items([('name', 'Harsh'), ('courses', ['arts'])])

for key in student:
    print(key)  # name  courses

for key, value in student.items():
    print(key, value)

'''
name Harsh
courses ['arts']
'''