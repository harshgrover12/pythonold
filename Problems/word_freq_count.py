def freq_word():
    str1 = input('Enter a string: ')
    li = str1.split()
    dict1 = {}
    for i in li:
        if i not in dict1:
            dict1[i] = 0
        dict1[i] += 1
    print(dict1)


print(freq_word())

'''
Sheena loves eating apple and mango. Her sister also loves eating apple and mango.
'''