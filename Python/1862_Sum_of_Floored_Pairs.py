# Author: Kaustav Ghosh
# Problem 1862: Sum of Floored Pairs

class Solution(object):
    def sumOfFlooredPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        max_val = max(nums)
        count = [0] * (max_val + 1)
        for x in nums:
            count[x] += 1
        # Prefix sum of counts
        prefix = [0] * (max_val + 2)
        for i in range(1, max_val + 1):
            prefix[i] = prefix[i - 1] + count[i]
        result = 0
        for x in range(1, max_val + 1):
            if count[x] == 0:
                continue
            mul = 1
            while mul * x <= max_val:
                lo = mul * x
                hi = min((mul + 1) * x - 1, max_val)
                cnt = prefix[hi] - prefix[lo - 1]
                result = (result + count[x] * mul * cnt) % MOD
                mul += 1
        return result
