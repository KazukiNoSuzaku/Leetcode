# Author: Kaustav Ghosh
# Problem: Jump Game VII
# Approach: dp[i] is reachable if some earlier reachable '0' lies in [i-maxJump, i-minJump]; a prefix count of reachable indices answers that window test in O(1)

class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        if s[-1] != '0':
            return False

        dp = [False] * n
        dp[0] = True
        prefix = [0] * (n + 1)  # prefix[i] = count of reachable indices < i
        prefix[1] = 1

        for i in range(1, n):
            if s[i] == '0':
                lo = max(0, i - maxJump)
                hi = i - minJump
                if hi >= 0 and prefix[hi + 1] - prefix[lo] > 0:
                    dp[i] = True
            prefix[i + 1] = prefix[i] + (1 if dp[i] else 0)

        return dp[n - 1]
