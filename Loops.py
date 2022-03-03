nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 2:
        print('Found!')
        break
    print(num)  # 1

for num in nums:
    if num == 3:
        continue
    print(num)  # 1 2 4 5

for num in nums:
    for char in 'abc':
        print(num, char)
'''
1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
4 a
4 b
4 c
5 a
5 b
5 c
'''

for i in range(10):
    print(i)  # it will iterate from 0 to 9

for i in range(1, 11):
    print(i)  # it will iterate from 1 to 10

x = 0
while x < 10:
    if x == 5:
        break
    print(x)  # 0 1 2 3 4
    x += 1

while True:
    if x == 5:
        break
    print(x)  # 0 1 2 3 4
    x += 1