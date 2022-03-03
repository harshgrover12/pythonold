def intersect1(a, b):
    l1 = len(a)
    l2 = len(b)
    list1 = []
    i = 0
    j = 0
    while i < l1 and j < l2:
        if a[i] == b[j]:
            list1.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
    return list1


print(intersect1([1, 2, 2, 3, 4, 5, 6], [3, 4]))
