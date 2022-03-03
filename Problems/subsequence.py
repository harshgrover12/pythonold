def subsequence(string):
    result = []
    l = len(string)
    if l == 0:
        return [" "]
    else:
        for i in subsequence(string[1:l]):
            result.append(i)
            result.append(string[0]+i)
    return(result)

print(subsequence('net'))