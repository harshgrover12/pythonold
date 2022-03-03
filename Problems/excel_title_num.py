def excel_title_num(str1):
    size = len(str1)
    result = 0
    for i in range(size):
        num = ord(str1[i]) - ord('A') + 1
        result = result + num * pow(26, size-1)
        size -= 1
    return result


str1 = 'Y'
print(excel_title_num(str1))