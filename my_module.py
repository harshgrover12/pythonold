print('Imported my_module')

test = 'Test String'


def find_index(target, search_list):
    '''find the index of value in a sequence'''
    for i, value in enumerate(search_list):
        if value == target:
            return i
    return -1

