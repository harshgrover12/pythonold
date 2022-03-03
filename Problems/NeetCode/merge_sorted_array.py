def merge(l1, m, l2, n):
    # last index l1
    last = m + n - 1
    p1 = m - 1
    p2 = n - 1

    # merge in reverse order
    while m > 0 and n > 0:
        if l1[p1] > l2[p2]:
            l1[last] = l1[p1]
            m -= 1
        else:
            l1[last] = l2[p2]
            n -= 1
        last -= 1
    # fill l1 with leftover l2 elements
    while n > 0:
        l1[last] = l2[p2]
        n, last = p2, last - 1


l1 = [1, 2, 3, 0, 0, 0]
l2 = [2, 5, 6]
m = 3
n = 3
print(merge(l1, m, l2, n))
