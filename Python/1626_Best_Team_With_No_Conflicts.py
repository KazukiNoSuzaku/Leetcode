# Author: Kaustav Ghosh
# https://leetcode.com/problems/best-team-with-no-conflicts/

class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        players = sorted(zip(ages, scores))
        n = len(players)
        dp = [0] * n
        for i in range(n):
            dp[i] = players[i][1]
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        return max(dp)
