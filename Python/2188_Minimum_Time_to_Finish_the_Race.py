# Author: Kaustav Ghosh
# Problem: Minimum Time to Finish the Race
# Approach: Precompute best[k], the cheapest time to run k consecutive laps on a single fresh tire (over all tires). A stint is only ever worth extending while the next lap costs less than changing tires and starting fresh, which bounds k to a small number. Then DP over laps: dp[i] is the minimum time to complete i laps, combining stints separated by changeTime (dp[0] seeded as -changeTime so the first stint pays no change)

class Solution(object):
    def minimumFinishTime(self, tires, changeTime, numLaps):
        """
        :type tires: List[List[int]]
        :type changeTime: int
        :type numLaps: int
        :rtype: int
        """
        INF = float('inf')
        # best[k] = min time for k consecutive laps on one tire, k >= 1
        # A stint length beyond the point where a single lap costs more than
        # (changeTime + f) is never optimal, so cap generously.
        max_stint = min(numLaps, 20)
        best = [INF] * (max_stint + 1)
        for f, r in tires:
            lap_cost = f
            total = 0
            k = 1
            while k <= max_stint:
                total += lap_cost
                if total < best[k]:
                    best[k] = total
                # cost of the next lap on this tire
                lap_cost *= r
                # if the next lap already exceeds a fresh-start lap, stop
                if lap_cost >= changeTime + f:
                    break
                k += 1

        dp = [INF] * (numLaps + 1)
        dp[0] = -changeTime  # first stint pays no change cost
        for i in range(1, numLaps + 1):
            limit = min(i, max_stint)
            for k in range(1, limit + 1):
                if best[k] == INF:
                    continue
                prev = dp[i - k]
                if prev != INF:
                    cand = prev + changeTime + best[k]
                    if cand < dp[i]:
                        dp[i] = cand
        return dp[numLaps]
