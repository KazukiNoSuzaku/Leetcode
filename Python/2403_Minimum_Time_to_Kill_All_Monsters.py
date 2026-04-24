import math

# Premium problem
# Bitmask DP: dp[mask] = minimum day on which we finish killing all monsters in mask.
# On day d, power = initialPower + (d-1)*gain.
# To kill monster i on day d: need (d-1)*gain >= power[i] - initialPower => d >= d_min[i].

class Solution:
    def minimumTime(self, power: list[int], initialPower: int, gain: int) -> int:
        n = len(power)
        d_min = [max(1, math.ceil(max(0, p - initialPower) / gain) + (1 if p > initialPower else 0))
                 for p in power]

        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == INF:
                continue
            for i in range(n):
                if mask >> i & 1:
                    continue
                next_day = max(dp[mask] + 1, d_min[i])
                new_mask = mask | (1 << i)
                if next_day < dp[new_mask]:
                    dp[new_mask] = next_day
        return dp[(1 << n) - 1]
