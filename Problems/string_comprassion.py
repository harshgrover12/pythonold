'''
String compression : Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would becine a2bc5a3. If the compressed string
would not become smaller than the original string, your method should return the original string
You can assume the string has only uppercase and lowercase letters(a-z).
'''


input_str_test_1 = "aabcccccaaa"
input_str_test_2 = "aaaaaabbccbcaabb"

def string_compression(input_str):
    comp_str = ""
    count = 1
    for i in range(len(input_str)-1):
        if input_str[i] == input_str[i+1]:  # a == a, count-2
            count += 1
        else:  # a != b at index 1 and 2 then comp_str would be a2
            comp_str += input_str[i] + str(count)
            count = 1
    comp_str += input_str[i] + str(count)  # last index would take code out of loop so this line

    if len(comp_str) >= len(input_str):
        return input_str
    else:
        return comp_str


print(string_compression(input_str_test_1))
print(string_compression(input_str_test_2))