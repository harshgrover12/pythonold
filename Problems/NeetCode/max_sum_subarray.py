class Solution:

    @staticmethod
    def max_subarray(arr1):
        max_subarr = arr1[0]
        curr_sum = 0

        for n in arr1:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_subarr = max(max_subarr, curr_sum)
        return max_subarr


s = Solution
print(s.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))