# Author: Kaustav Ghosh
# Problem: Best Team With No Conflicts
# Approach: Sort players by (age, score); a conflict-free team is then a non-decreasing-score subsequence, so run a max-sum LIS-style DP

class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        players = sorted(zip(ages, scores))
        n = len(players)
        dp = [score for _, score in players]  # best total ending at each player
        for i in range(n):
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        return max(dp)
