# Author: Kaustav Ghosh
# Problem: Get Maximum in Generated Array
# Approach: Build the array by its recurrence (even index copies nums[i/2], odd adds the next), tracking the running maximum

class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
        return max(nums)
