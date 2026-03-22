# Author: Kaustav Ghosh

class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        MOD = 10 ** 9 + 7

        def rev(n):
            r = 0
            while n:
                r = r * 10 + n % 10
                n //= 10
            return r

        diffs = Counter()
        for n in nums:
            diffs[n - rev(n)] += 1
        res = 0
        for cnt in diffs.values():
            res = (res + cnt * (cnt - 1) // 2) % MOD
        return res
