n = int(input('Enter number:'))

temp = n
rev = 0

while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n//10
if temp == rev:
    print('The number is palindrome')
else:
    print('The number is not palindrome')

# for input_num in range(6):
#     for i in range(input_num):
#         print(input_num, end=' ')
#     print('\n')

# def pattern_print(n):
#     for i in range(0, n):
#         for j in range(0, i+1):
#             print('#', end='')
#         print('\r')


# pattern_print(5)

# sum1 = 0
# number_input = int(input('Enter a number: '))
# temp = number_input
#
# while(number_input):
#     i = 1
#     fact = 1
#     rem = number_input % 10
#     while i <= rem:
#         fact = fact*i
#         i = i+1
#     sum1 = sum1 + fact
#     number_input //= 10
#
# if sum1 == temp:
#     print('strong number')
# else:
#     print('not a strong number')

# input_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#
# n = 4
#
# out = [input_list[i:i + n] for i in range(0,len(input_list), n)]
#
# print(out)

# def fib_gen():
#     a = 0
#     b = 1
#     while True:
#         c = a
#         a = b
#         b = c + a
#         yield c
#
#
# f = fib_gen()
# for i in range(20):
#     print(next(f), end=' ')
# list1 =[4,2,7,9]
# list2 = []
# print(list1)
# for i in range(len(list1)-1,-1,-1):
#     list2.append(list1[i])
# print(list2)

# num = int(input('Enter the number: '))
# for row in range(num,0,-1):
#     for col in range(1, row+1):
#         print('*', end ='')
#     print()

# num = int(input('Enter the number: '))
# for row in range(1, num + 1):
#     for col in range(1, num-row+1):
#         print(end=' ')
#     for col in range(1, row +1):
#         print('*', end= " ")
#     print()
#
#
# for row in range(1,6):
#     for col in range(row, 0, -1):
#         print(col, end=' ')
#     print()
