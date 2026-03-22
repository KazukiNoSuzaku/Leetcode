# Author: Kaustav Ghosh

class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from math import gcd
        max_val = max(nums)
        num_set = set(nums)
        count = 0
        for g in range(1, max_val + 1):
            cur_gcd = 0
            for mult in range(g, max_val + 1, g):
                if mult in num_set:
                    cur_gcd = gcd(cur_gcd, mult)
                    if cur_gcd == g:
                        break
            if cur_gcd == g:
                count += 1
        return count
