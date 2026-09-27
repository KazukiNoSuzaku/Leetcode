# Author: Kaustav Ghosh
# Problem: Minimum Total Distance Traveled
# Approach: In an optimal plan neither robots nor factories cross, so sorting both sides lets a factory take a contiguous block of robots. dp[j] is the cheapest way to repair the first j robots with the factories considered so far, and each factory extends it by taking between one and its limit of the next robots, adding their walking distances

class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robots = sorted(robot)
        m = len(robots)
        INF = float('inf')
        dp = [0] + [INF] * m
        for position, limit in sorted(factory):
            for j in range(m, 0, -1):
                distance = 0
                for taken in range(1, min(limit, j) + 1):
                    distance += abs(robots[j - taken] - position)
                    if dp[j - taken] != INF:
                        dp[j] = min(dp[j], dp[j - taken] + distance)
        return dp[m]
