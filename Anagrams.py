def anagram(A):
    if A is None:
        return
    else:
        dict1 = {}
        word_list = [''.join(sorted(item)) for item in A]
        # word_list: ['act', 'dgo', 'dgo', 'act', 'act']
        for i in range(len(word_list)):
            if word_list[i] not in dict1:
                dict1[word_list[i]] = [i]

            else:
                dict1[word_list[i]].append(i)
    return dict1


print(anagram(['cat', 'dog', 'god', 'tca', 'act']))
