# Author: Kaustav Ghosh
# Problem 2012: Sum of Beauty in the Array

class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # prefix_max[i] = max of nums[0..i]
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        # suffix_min[i] = min of nums[i..n-1]
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        result = 0
        for i in range(1, n - 1):
            if prefix_max[i - 1] < nums[i] < suffix_min[i + 1]:
                result += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                result += 1
        return result
