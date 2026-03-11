# Count schemes using at most n members achieving at least minProfit.

# Author: Kaustav Ghosh

class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for members in range(n, -1, -1):
                for pro in range(minProfit, -1, -1):
                    if dp[members][pro]:
                        nm = min(members + g, n)
                        np = min(pro + p, minProfit)
                        dp[nm][np] = (dp[nm][np] + dp[members][pro]) % MOD
        return sum(dp[m][minProfit] for m in range(n + 1)) % MOD
