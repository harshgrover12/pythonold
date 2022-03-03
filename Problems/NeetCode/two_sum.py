class Solution:

    @staticmethod
    def two_sum(lst1, target):
        prev_map = {}

        for i, n in enumerate(lst1):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i


s = Solution
print(s.two_sum([1, 3, 4, 5], 6))
