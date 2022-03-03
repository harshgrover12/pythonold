def common_elements(l1, l2):
    l3 = []
    count = 0
    for i in l1:
        for j in l2:
            if i == j:
                l3.append(i)
                count += 1
    print(count)
    return l3


l1 = [2, 4, 6, 8, 10, 12]
l2 = [3, 6, 9, 12, 15, 18]
print(common_elements(l1, l2))
'''
time complexity - o(n*m)
space complexity - o(1)
'''


def common_elements_dict(l1, l2):
    dict1 = dict.fromkeys(l1, 1)

    count = 0
    for element in l2:
        if dict1.get(element) is not None:
            print(element, end=' ')
            count += 1
    print()
    print(count)


l1 = [2, 4, 6, 8, 10, 12]
l2 = [3, 6, 9, 12, 15, 18]
print(common_elements_dict(l1, l2))

