nums = [1, 11, 3, 2, 7]
target = 4

def two_sum(nums, target):
    if len(nums) <= 1:
        return False
    aux_dict = {}
    for i in range(len(nums)):  # [0,1,2,3,4]
        if not nums[i] in aux_dict:  # nums[0]=1, nums[1]=3, nums[2]=11, nums[3]=2, nums[4]=7
            aux_dict[target - nums[i]] = i  # aux_dict[4-1]=0
        else:
            return [aux_dict[nums[i]], i]  # [0,1]


print(two_sum(nums, target))