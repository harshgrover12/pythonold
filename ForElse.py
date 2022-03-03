my_list = [1,2,3,4,5]

for i in my_list:
    print(i)
    if i == 3:
        break
else:
    print('Hit the For/Else statement')

'''
1
2
3
4
5
Hit the For/Else statement

This is when there is no break logic added and when break is added in the code,
then else statement will not execute.

Same applies for While-Else loop.
'''


def find_index(search_list, target):
    for index, value in enumerate(search_list):
        if value == target:
            break
    else:
        return -1
    return index


my_list = ['Corey', 'Rick', 'John']
index_location = find_index(my_list, 'Rick')  #  Location of target is index: 1
# index_location = find_index(my_list, 'Steve')  # Location of target is index: -1, as it will go to else block
print('Location of target is index: {}'.format(index_location))