# Author: Kaustav Ghosh
# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

from bisect import bisect_left, bisect_right

class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        total = prefix[n]
        result = 0
        for i in range(1, n - 1):
            left_sum = prefix[i]
            if left_sum * 3 > total:
                break
            # Find minimum j such that prefix[j] - prefix[i] >= prefix[i]
            lo = bisect_left(prefix, 2 * left_sum, i + 1, n)
            # Find maximum j such that prefix[n] - prefix[j] >= prefix[j] - prefix[i]
            # i.e. prefix[j] <= (total + prefix[i]) / 2
            hi = bisect_right(prefix, (total + left_sum) // 2, i + 1, n) - 1
            if lo <= hi:
                result = (result + hi - lo + 1) % MOD
        return result
