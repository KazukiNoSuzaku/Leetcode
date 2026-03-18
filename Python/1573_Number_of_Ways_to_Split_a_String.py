# Author: Kaustav Ghosh
# Problem: 1573 - Number of Ways to Split a String
# Approach: Count 1s, find split points for exactly thirds

class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        ones = s.count('1')

        if ones % 3 != 0:
            return 0

        n = len(s)
        if ones == 0:
            # Choose 2 cut positions from n-1 gaps
            return (n - 1) * (n - 2) // 2 % MOD

        target = ones // 3
        # Find positions of 1st/2nd target boundary and 2nd/3rd target boundary
        positions = [i for i, c in enumerate(s) if c == '1']
        # Between end of first third and start of second third
        gap1 = positions[target] - positions[target - 1]
        gap2 = positions[2 * target] - positions[2 * target - 1]

        return gap1 * gap2 % MOD
