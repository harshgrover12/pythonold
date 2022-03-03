def reverse(str1):
    str_r = str1[::-1]
    return str_r


def reverse_words(str1):
    n = len(str1)
    if n == 1:
        return str1
    lst1 = str1.split(" ")
    size = len(lst1)
    rev_all = ""
    for i in range(size):
        rev = (lst1[i])[::-1]
        print(rev)
        '''
        SOESTEN
        SI
        TNELLECXE
        '''
        rev_all = rev_all + rev + " "
        print(rev_all)  # SOESTEN SI TNELLECXE

    rev_all = rev_all[::-1]
    return rev_all.strip()



str1 = 'Harsh Grover'
# print(reverse(str1))
print(reverse_words(str1))  # Grover Harsh