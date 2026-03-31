# Author: Kaustav Ghosh
# 2188. Minimum Time to Finish the Race
# https://leetcode.com/problems/minimum-time-to-finish-the-race/
# Difficulty: Hard
#
# Approach: DP with tire change cost.
# 1. Precompute best[r] = minimum time to run exactly r laps on a single tire
#    (without changing). Stop when time degradation makes it worse than just
#    using fastest tire for 1 lap.
# 2. dp[i] = minimum time to finish i laps total.
#    dp[i] = min over j in [1..i] of (dp[i-j] + changeTime + best[j])
#    For i == j (all laps on first tire), no changeTime is added at start.
# Time: O(n * log(n)), Space: O(n)

class Solution(object):
    def minimumFinishTime(self, tires, changeTime, numLaps):
        """
        :type tires: List[List[int]]
        :type changeTime: int
        :type numLaps: int
        :rtype: int
        """
        INF = float('inf')
        # best[r] = min time to run r laps consecutively on one tire
        # r is at most ~18 because f^r grows exponentially
        max_laps_single = 18
        best = [INF] * (max_laps_single + 1)

        for f, r in tires:
            time = r
            for lap in range(1, max_laps_single + 1):
                if time > (changeTime + r):
                    break
                if time < best[lap]:
                    best[lap] = time
                time += r * (f ** lap)

        dp = [INF] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            for j in range(1, min(i, max_laps_single) + 1):
                if best[j] < INF:
                    dp[i] = min(dp[i], dp[i - j] + changeTime + best[j])

        return dp[numLaps] - changeTime
