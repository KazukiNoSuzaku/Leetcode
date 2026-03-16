# Author: Kaustav Ghosh
# Problem: Number of Subsequences That Satisfy the Given Sum Condition
# Approach: Sort, two pointers, count 2^(right-left) for valid pairs

class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        power = [1] * n
        for i in range(1, n):
            power[i] = power[i - 1] * 2 % MOD

        result = 0
        left, right = 0, n - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + power[right - left]) % MOD
                left += 1
            else:
                right -= 1
        return result
