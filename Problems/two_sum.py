def two_sum(arr, sum):
    arr.sort()
    left = 0
    right = len(arr)-1
    while left <= right:
        if arr[left] + arr[right] > sum:
            right -= 1
        elif arr[left] + arr[right] < sum:
            left += 1
        elif arr[left] + arr[right] == sum:
            print('values of pair are', arr[left], 'and', arr[right], 'which equals to', sum)
            right = right - 1
            left = left + 1


# arr = [5, 7, 4, 3, 9, 8, 19, 21]
arr = [2, 3, 3, 7, 8, 9]
sum = 10
two_sum(arr, sum)

'''
values of pair are 2 and 8 which equals to 10
values of pair are 3 and 7 which equals to 10
time = o(n)
sort = o(nlogn)
time complexity T(n) = o(nlogn)
space complexity = o(1)
'''
