def find_pivot(left, right, arr):
    if left > right:
        return -1
    if left == right:
        return left
    mid = (left + right)//2
    if (mid<right and arr[mid]>arr[mid+1]):
        return mid + 1
    else:
        if (arr[left] > arr[mid]):
            return find_pivot(left, mid, right)
        else:
            return find_pivot(mid+1, right, arr)

arr = [7,9,11,13,15,17,19,1,3,5]
find_pivot(0, len(arr)-1, arr)