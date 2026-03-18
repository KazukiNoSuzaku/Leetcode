# Author: Kaustav Ghosh
# Problem: 1513 - Number of Substrings With Only 1s
# Approach: sum k*(k+1)/2 for each run of consecutive 1s

class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        result = 0
        count = 0
        for c in s:
            if c == '1':
                count += 1
                result += count
            else:
                count = 0
        return result % MOD
