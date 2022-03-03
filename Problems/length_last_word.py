def len_last_word(a):
    arr = a.split(' ')
    last_word = arr[-1]
    if len(arr) == 1:
        print(len(a))
    else:
        print(len(last_word))


a = 'Hello Netsetos'
len_last_word(a)