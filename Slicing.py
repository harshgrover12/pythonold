my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[5])
print(my_list[-1])
# list[start:end:step]
print(my_list[0:5])
print(my_list[0:7:2])
print(my_list[-7:8])
print(my_list[1:])  # 1 to end of the list
print(my_list[:])   # full list
print(my_list[2:-1:-1])  # []
print(my_list[-1:2:-1])  # [9, 8, 7, 6, 5, 4, 3]
print(my_list[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

sample_url = 'http://coreyms.com'
print(sample_url)

print(sample_url[::-1])
print(sample_url.split('.')[-1])  # sample_url[-4:]
print(sample_url.split('://')[1])  # sample_url[7:]
print(sample_url.split('://')[1].split('.')[0])  # sample_url[7:-4]
