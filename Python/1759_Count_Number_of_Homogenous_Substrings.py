# Author: Kaustav Ghosh

class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        res = 0
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            res = (res + count) % MOD
        return (res + 1) % MOD
