# Author: Kaustav Ghosh
# Problem: Best Team With No Conflicts
# Approach: A conflict is a younger player outscoring an older one, so once the players are sorted by age the chosen team must have non-decreasing scores in that order, which turns the problem into a maximum-sum non-decreasing subsequence. Ties in age need care: sorting equal ages by score as well means that among players of the same age the order is already non-decreasing, so no pair of them can ever be judged a conflict, which is correct since two players of the same age never conflict whatever their scores. The running total for each player is then its own score plus the best total among earlier players scoring no more than it.

class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        players = sorted(zip(ages, scores))
        n = len(players)
        best_ending = [0] * n
        answer = 0
        for i in range(n):
            score = players[i][1]
            running = score
            for j in range(i):
                if players[j][1] <= score and best_ending[j] + score > running:
                    running = best_ending[j] + score
            best_ending[i] = running
            if running > answer:
                answer = running
        return answer
