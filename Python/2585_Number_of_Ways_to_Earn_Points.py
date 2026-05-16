class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for count, marks in types:
            # Iterate in reverse to avoid using same type twice in one pass
            for j in range(target, -1, -1):
                if dp[j] == 0:
                    continue
                for take in range(1, count + 1):
                    if j + take * marks > target:
                        break
                    dp[j + take * marks] = (dp[j + take * marks] + dp[j]) % MOD
        return dp[target]
