# Author: Kaustav Ghosh
# Problem: Count Number of Special Subsequences
# Approach: Track counts of subsequences currently ending in the 0-block, the 1-block, and the full 0-1-2 form. A 0 doubles the 0-block and seeds a new one; a 1 doubles the 1-block and extends any 0-block; a 2 doubles and extends the 1-block

class Solution(object):
    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        d0 = d1 = d2 = 0
        for x in nums:
            if x == 0:
                d0 = (2 * d0 + 1) % MOD
            elif x == 1:
                d1 = (2 * d1 + d0) % MOD
            else:
                d2 = (2 * d2 + d1) % MOD
        return d2
