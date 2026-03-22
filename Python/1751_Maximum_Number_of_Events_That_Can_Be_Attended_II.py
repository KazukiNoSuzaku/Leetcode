# Author: Kaustav Ghosh

class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        import bisect
        events.sort(key=lambda x: x[1])
        n = len(events)
        ends = [e[1] for e in events]
        # dp[i][j] = max value using first i events attending at most j
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            start_i = events[i - 1][0]
            val_i = events[i - 1][2]
            # Find last event that ends before start_i
            prev = bisect.bisect_left(ends, start_i, 0, i - 1)
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i - 1][j], dp[prev][j - 1] + val_i)
        return dp[n][k]
