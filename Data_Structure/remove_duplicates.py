def remove_duplicates_space(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr
    temp = [0] * n
    pivot = 0
    for last_o in range(0, n-1):
        if arr[last_o] != arr[last_o + 1]:
            temp[pivot] = arr[last_o]
            pivot += 1
    temp[pivot] = arr[n-1]
    return temp[0:pivot+1]


arr = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 5]
print(remove_duplicates_space(arr))
'''
Output: [1,2,3,4,5]
Above function will take o(n) space
'''

'''
Below function will run with space complexity of o(1)
as we are using same array for replacing elements.

'''


def remove_duplicates(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr
    pivot = 0
    for last_o in range(0, n-1):
        if arr[last_o] != arr[last_o + 1]:
            arr[pivot] = arr[last_o]
            pivot += 1
    arr[pivot] = arr[n-1]
    return arr[0:pivot+1]


arr = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 5]
print(remove_duplicates(arr))


def drop_duplicates(ls1):
    count = 0
    dct = {}
    for i in range(len(ls1)):
        if ls1[i] not in dct.values():
            dct[count] = ls1[i]
            count += 1
    return list(dct.values())


arr = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 5]
print(drop_duplicates(arr))

print(list(set(arr)))  # [1,2,3,4,5]
