# Author: Kaustav Ghosh
# Problem: Count Nice Pairs in an Array
# Approach: The nice condition rearranges to x - rev(x) being equal for both elements, so count pairs sharing that key with a running counter

from collections import Counter

class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        seen = Counter()
        total = 0
        for x in nums:
            key = x - int(str(x)[::-1])
            total += seen[key]
            seen[key] += 1
        return total % MOD
