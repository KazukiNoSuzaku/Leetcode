# Author: Kaustav Ghosh
# Problem: Make Sum Divisible by P
# Approach: We need the shortest subarray whose sum mod p equals total mod p; track prefix remainders and their latest index in a map

class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        target = sum(nums) % p
        if target == 0:
            return 0

        n = len(nums)
        last = {0: -1}
        prefix = 0
        best = n
        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            need = (prefix - target) % p
            if need in last:
                best = min(best, i - last[need])
            last[prefix] = i

        return best if best < n else -1
