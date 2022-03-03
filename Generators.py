# def square_numbers(nums):
#     result = [n*n for n in nums]
#     return result
#
# my_nums = square_numbers([1,2,3,4,5])
# print(my_nums)

# Generator
# def square_numbers(nums):
#     for i in nums:
#         yield i*i

# my_nums = square_numbers([1,2,3,4,5])
my_nums = (n*n for n in [1,2,3,4,5])
print(my_nums)  # generator object square_numbers at 0x0000023B2597D3C8>
print(list(my_nums))  # [1, 4, 9, 16, 25]
# Generator don't hold all the values, returns one at time
# print(next(my_nums))  # 1
# print(next(my_nums))  # 4
# print(next(my_nums))  # 9
# print(next(my_nums))  # 16
# print(next(my_nums))  # 25
# print(next(my_nums))  # StopIteration
for num in my_nums:
    print(num)  # for loop does the same as above but it handles StopIteration exception.


