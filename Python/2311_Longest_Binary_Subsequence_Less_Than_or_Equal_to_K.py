# Author: Kaustav Ghosh
# 2311. Longest Binary Subsequence Less Than or Equal to K
# Greedy: take all 0s, then take rightmost 1s while value <= k

class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # All 0s can always be included (they don't increase value)
        zeros = s.count('0')

        # Now greedily take 1s from the right (least significant positions)
        # We pick 1s starting from the rightmost, building the binary number
        ones = 0
        value = 0
        power = 0

        for c in reversed(s):
            if c == '1':
                if value + (1 << power) <= k:
                    value += (1 << power)
                    ones += 1
            power += 1

        return zeros + ones
