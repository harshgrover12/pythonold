def redundant_braces(str1):
    st = []
    for i in range(len(str1)):
        if str1[i] in '(+-*/':
            st.append(str1[i])
        elif str1[i] == ')':
            if st.pop() == '(':
                return 1
            st.pop()
    return 0


# a = redundant_braces('((a+b))')  # redundant
# a = redundant_braces('((a)+b)')  # redundant
a = redundant_braces('((a+b)*c)')  # not redundant
if a == 1:
    print('redundant braces')
else:
    print('not redundant')