# Author: Kaustav Ghosh
# Problem: First Day Where You Have Been in All the Rooms
# Approach: dp[i] is the first day you enter room i. Reaching i from i-1 costs one day to bounce back to nextVisit[i-1], the days to return from there to i-1, and one day forward: dp[i] = 2*dp[i-1] - dp[nextVisit[i-1]] + 2

class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        """
        :type nextVisit: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nextVisit)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD
        return dp[n - 1] % MOD
