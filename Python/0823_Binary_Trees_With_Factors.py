# Count binary trees where each node value is product of its children, from given array.

# Author: Kaustav Ghosh

class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        for x in arr:
            dp[x] = 1
            for left in dp:
                if x % left == 0 and x // left in dp:
                    dp[x] += dp[left] * dp[x // left]
        return sum(dp.values()) % MOD
