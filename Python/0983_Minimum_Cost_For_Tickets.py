# You travel on certain days. Buy 1, 7, or 30-day passes.
# Return the minimum cost to travel on all required days.

# Author: Kaustav Ghosh

class Solution(object):
    def mincostTickets(self, days, costs):
        day_set = set(days)
        dp = [0] * 366
        for i in range(1, 366):
            if i not in day_set:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(
                    dp[i-1] + costs[0],
                    dp[max(0, i-7)] + costs[1],
                    dp[max(0, i-30)] + costs[2]
                )
        return dp[days[-1]]
