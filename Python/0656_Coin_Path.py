# Find lexicographically smallest path from index 1 to n with max jump B and cost constraint.

# Author: Kaustav Ghosh

class Solution(object):
    def cheapestJump(self, coins, maxJump):
        n = len(coins)
        if coins[n-1] == -1: return []
        dp = [float('inf')] * n
        nxt = [-1] * n
        dp[n-1] = coins[n-1]
        for i in range(n-2, -1, -1):
            if coins[i] == -1: continue
            for j in range(i+1, min(i+maxJump+1, n)):
                if dp[j] == float('inf'): continue
                cost = coins[i] + dp[j]
                if cost < dp[i]:
                    dp[i] = cost
                    nxt[i] = j
        if dp[0] == float('inf'): return []
        path = []
        i = 0
        while i != -1:
            path.append(i + 1)
            i = nxt[i]
        return path
