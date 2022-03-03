print('Imprted my_module')

test = 'Test String'

def find_index(target,to_search):
    '''find the index of value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1