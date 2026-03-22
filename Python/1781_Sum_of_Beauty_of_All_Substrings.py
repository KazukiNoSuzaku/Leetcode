# Author: Kaustav Ghosh

class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            count = [0] * 26
            for j in range(i, len(s)):
                count[ord(s[j]) - ord('a')] += 1
                active = [c for c in count if c > 0]
                res += max(active) - min(active)
        return res
