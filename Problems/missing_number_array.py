def get_missing_number_summation(a):
    a = sorted(a)
    n = a[-1]  # 7
    total = n*(n + 1)//2  # 28
    sum1 = 0
    sum1 = sum(a)  # 25
    print(total-sum1)  # 3


def get_missing_number_xor(a):
    xor_a = a[0]
    for index in range(1, len(a)):
        xor_a = xor_a ^ a[index]
    x2 = 0
    for index in range(1, len(a)+2):
        x2 = x2 ^ index
    print(xor_a ^ x2)

def missingnumber(givenlist):
    sorted_list = sorted(givenlist)
    print('The given list is:', givenlist)
    print('The sorted list is:', sorted_list)
    newlist = list(range(sorted_list[0], sorted_list[-1]+1))
    print('the newlist is in range of ', newlist)
    missing_number_given_list = set(givenlist) ^ set(newlist)
    print('missing number in given list', missing_number_given_list)

missingnumber([3,1,5])


# a = [1, 2, 4, 5, 6, 7]
# get_missing_number_summation(a)
# get_missing_number_xor(a)
