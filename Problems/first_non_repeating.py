def first_non_repeating(str1):
    dict1 = {}
    for i in range(len(str1)):
        key = str1[i]
        if key not in dict1:
            dict1[key] = 1
        else:
            dict1[key] += 1
    print(dict1)
    # for key, value in dict1.items():
    #     if value == 1:
    #         return key, value
    for index in range(len(str1)):
        if dict1[str1[index]] == 1:
            return str1[index], index  # ('M', 12)


print(first_non_repeating('NETSETOOSNETM'))