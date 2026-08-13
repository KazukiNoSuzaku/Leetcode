# Author: Kaustav Ghosh
# Problem: Sum of Beauty in the Array
# Approach: Precompute prefix maxima and suffix minima. Beauty is 2 when nums[i] exceeds everything on its left and is below everything on its right, else 1 when it strictly sits between its immediate neighbors, else 0

class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix_max = [0] * n
        suffix_min = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        total = 0
        for i in range(1, n - 1):
            if prefix_max[i - 1] < nums[i] < suffix_min[i + 1]:
                total += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                total += 1
        return total
