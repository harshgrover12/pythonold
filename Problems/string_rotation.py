'''
string rotation: Given two strings, s1 and s2, write code to check if s2 is rotation f s1
e.g- 'waterbottle is a rotation of erbottlewat
'''

test_rot_str1 = 'waterbottle'
test_rot_str2 = 'erbottlewat'

test_rot_str3 = 'watertables'
test_rot_str4 = 'erbottlewat'

import string


def is_string_rotation(str1, str2):

    if len(str1) != len(str2):
        return False

    str1 = str1.lower()
    str2 = str2.lower()

    dict1 = dict.fromkeys(list(string.ascii_lowercase), 0)
    dict2 = dict.fromkeys(list(string.ascii_lowercase), 0)

    for i in range(len(str1)):
        dict1[str1[i]] += 1
        dict2[str2[i]] += 1
    return dict1 == dict2


print(is_string_rotation(test_rot_str1,test_rot_str2))  # True
print(is_string_rotation(test_rot_str3, test_rot_str4))  # False


def left_rotated_string(name):
    size = len(name)
    temp = name + name

    for i in range(size):
        for j in range(size):
            print(temp[i+j], end='')
        print()


str1 = 'NETSET'
left_rotated_string(str1)