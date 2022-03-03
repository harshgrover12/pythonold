
from Data_Structure.util import time_it


@time_it
def linear_search(numbers_list, number_to_find):
    for ind, ele in enumerate(numbers_list):
        if ele == number_to_find:
            return ind
        break
    return -1



def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list)-1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index)//2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index
        elif mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    else:
        return -1

'''
mid = left+ (right-left)//2
'''
# recursion function will not have loops
def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    elif mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)


if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 17
    # numbers_list = [i for i in range(1000001)]
    # number_to_find = 100000
    # index = linear_search(numbers_list, number_to_find)
    # print(f"Number found at index {index} using linear search")
    # index = binary_search(numbers_list, number_to_find)
    # print(f"Number found at index {index} using binary search")
    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index {index} using recursive binary search")

'''
linear_search took 52.895307540893555 ms
Number found at index None using linear search
binary_search took 0.0 ms
Number found at index None using binary search
'''