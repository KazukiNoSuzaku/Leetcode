# Author: Kaustav Ghosh
# Problem: Minimum Sideway Jumps
# Approach: DP over lanes holding the min jumps to be in each lane at the current point. At each step block the obstacle lane, then any open lane can also be reached by one jump from the cheapest open lane

class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        INF = float('inf')
        dp = [1, 0, 1]  # start in lane 2 (index 1) with no jumps

        for i in range(1, len(obstacles)):
            obs = obstacles[i]
            if obs:
                dp[obs - 1] = INF
            cheapest = min(dp[j] for j in range(3) if obs == 0 or j != obs - 1)
            for lane in range(3):
                if obs == 0 or lane != obs - 1:
                    dp[lane] = min(dp[lane], cheapest + 1)

        return min(dp)
