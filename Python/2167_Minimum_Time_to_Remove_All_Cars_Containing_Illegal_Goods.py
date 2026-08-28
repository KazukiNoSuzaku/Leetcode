# Author: Kaustav Ghosh
# Problem: Minimum Time to Remove All Cars Containing Illegal Goods
# Approach: For a prefix, clearing illegal cars costs either the running per-car cost (2 each) or removing the whole prefix from the left (its length). Compute this prefix cost and the symmetric suffix cost, then combine them over every split point

class Solution(object):
    def minimumTime(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        prefix = [0] * n
        run = 0
        for i in range(n):
            run = min(run + (2 if s[i] == '1' else 0), i + 1)
            prefix[i] = run

        suffix = [0] * n
        run = 0
        for i in range(n - 1, -1, -1):
            run = min(run + (2 if s[i] == '1' else 0), n - i)
            suffix[i] = run

        ans = min(prefix[n - 1], suffix[0])
        for i in range(n - 1):
            ans = min(ans, prefix[i] + suffix[i + 1])
        return ans
