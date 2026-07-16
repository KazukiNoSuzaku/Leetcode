# Author: Kaustav Ghosh
# Problem: Maximum Number of Events That Can Be Attended II
# Approach: Sort events by end day; dp[j][i] = best value from the first i events attending at most j. Taking event i jumps back to the last event ending before it starts, found by binary search

from bisect import bisect_right

class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort(key=lambda e: e[1])
        n = len(events)
        ends = [e[1] for e in events]

        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for j in range(1, k + 1):
            for i in range(1, n + 1):
                start, _, value = events[i - 1]
                prev = bisect_right(ends, start - 1)  # events fully finished before start
                dp[j][i] = max(dp[j][i - 1], dp[j - 1][prev] + value)
        return dp[k][n]
