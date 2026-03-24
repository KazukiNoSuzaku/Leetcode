# Author: Kaustav Ghosh
# Problem 1997: First Day Where You Have Been in All the Rooms

class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        """
        :type nextVisit: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nextVisit)
        # dp[i] = first day we visit room i
        dp = [0] * n
        for i in range(1, n):
            # dp[i] = 2*dp[i-1] - dp[nextVisit[i-1]] + 2
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD
        return dp[n - 1]
