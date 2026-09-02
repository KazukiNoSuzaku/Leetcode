# Author: Kaustav Ghosh
# Problem: Number of Ways to Select Buildings
# Approach: Valid selections are the alternating length-3 subsequences "010" and "101". Sweep left to right tracking counts of single characters and of the two-character subsequences "01" and "10"; each new character extends a matching pair into a full alternating triple

class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        c0 = c1 = 0        # counts of '0' and '1' seen so far
        c01 = c10 = 0      # counts of subsequences "01" and "10"
        ans = 0
        for ch in s:
            if ch == '1':
                ans += c10       # "10" + "1" -> "101"
                c01 += c0        # "0" + this "1" -> "01"
                c1 += 1
            else:
                ans += c01       # "01" + "0" -> "010"
                c10 += c1        # "1" + this "0" -> "10"
                c0 += 1
        return ans
