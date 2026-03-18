# Author: Kaustav Ghosh
# Problem: 1590 - Make Sum Divisible by P
# Approach: Prefix sum mod p, find shortest subarray with matching remainder

class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums) % p
        if total == 0:
            return 0

        n = len(nums)
        seen = {0: -1}
        prefix = 0
        result = n

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - total) % p
            if target in seen:
                result = min(result, i - seen[target])
            seen[prefix] = i

        return result if result < n else -1
