# Author: Kaustav Ghosh
# Problem: Minimum Skips to Arrive at Meeting On Time
# Approach: DP on (road, skips) storing elapsed time * speed as integers. After a non-final road a rest rounds elapsed up to a whole hour (multiple of speed); skipping the rest costs a skip but avoids the rounding

class Solution(object):
    def minSkips(self, dist, speed, hoursBefore):
        """
        :type dist: List[int]
        :type speed: int
        :type hoursBefore: int
        :rtype: int
        """
        n = len(dist)
        INF = float('inf')
        dp = [0] + [INF] * n  # dp[j] = min elapsed*speed with j skips

        for i, d in enumerate(dist):
            nxt = [INF] * (n + 1)
            last = i == n - 1
            for j in range(i + 1):
                if dp[j] == INF:
                    continue
                if last:
                    nxt[j] = min(nxt[j], dp[j] + d)
                else:
                    # skip the rest: no rounding, one more skip
                    nxt[j + 1] = min(nxt[j + 1], dp[j] + d)
                    # take the rest: round up to the next full hour
                    rounded = (dp[j] + d + speed - 1) // speed * speed
                    nxt[j] = min(nxt[j], rounded)
            dp = nxt

        limit = hoursBefore * speed
        for j in range(n + 1):
            if dp[j] <= limit:
                return j
        return -1
