def largest_number(list1):
    for i, n in enumerate(list1):
        list1[i] = str(n)

    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1

    nums = sorted(list1, key=cmp_to_key(compare()))
