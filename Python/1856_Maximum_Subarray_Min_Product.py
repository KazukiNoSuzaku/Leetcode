# Author: Kaustav Ghosh
# Problem 1856: Maximum Subarray Min-Product

class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        # Find left and right boundaries using monotonic stack
        left = [-1] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                right[stack.pop()] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        result = 0
        for i in range(n):
            total = prefix[right[i]] - prefix[left[i] + 1]
            result = max(result, nums[i] * total)
        return result % MOD
