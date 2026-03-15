# Schedule jobs over d days. Each day must have at least one job.
# Day difficulty = max job difficulty that day. Minimize total difficulty.

# Author: Kaustav Ghosh

class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d: return -1
        INF = float('inf')
        dp = [INF] * n
        # Base: first day covers jobs 0..i
        cur_max = 0
        for i in range(n):
            cur_max = max(cur_max, jobDifficulty[i])
            dp[i] = cur_max
        for day in range(1, d):
            new_dp = [INF] * n
            for i in range(day, n):
                cur_max = 0
                for j in range(i, day - 1, -1):
                    cur_max = max(cur_max, jobDifficulty[j])
                    if dp[j-1] < INF:
                        new_dp[i] = min(new_dp[i], dp[j-1] + cur_max)
            dp = new_dp
        return dp[n-1]
