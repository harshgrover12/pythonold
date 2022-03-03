
def max_product(lst1):
    res = max(lst1)
    cur_min, cur_max = 1, 1

    for n in lst1:
        if n == 0:
            cur_min, cur_max = 1, 1
            continue
        tmp = cur_max * n
        cur_max = max(tmp, n*cur_min, n)
        cur_min = min(tmp, n*cur_min, n)
        res = max(res, cur_max)
    return res


print(max_product([1, 2, -3, 4, 5]))




