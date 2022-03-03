def max_sum_subarray(arr1):
    size = len(arr1)
    curr_sum = 0
    max_so_far = arr1[0]
    st = 0;en = 0;poi = 0
    for i in range(0, size):
        curr_sum = curr_sum + arr1[i]

        if curr_sum > max_so_far:
            max_so_far = curr_sum
            st = poi  # wherever curr_sum will be set to 0, start point will be after that element
            en = i
        if curr_sum < 0:
            curr_sum = 0
            poi = i + 1

    print('Maximum sum subarray is', max_so_far)
    print('Start index of window is', st)
    print('End index of window is', en)


arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]
max_sum_subarray(arr)

'''
Maximum sum subarray is 7
Start index of window is 3
End index of window is 8
'''