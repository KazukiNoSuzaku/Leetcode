# Author: Kaustav Ghosh
# Problem: Minimum Sideway Jumps
# Approach: The frog always advances one point at a time, so the only decision is which lane to occupy at each point, and the cost of being in a lane there depends only on the costs one point earlier. Each point is handled in two stages: a lane holding an obstacle becomes unreachable, and then every surviving lane can also be entered by paying one jump from the cheapest other lane. Taking that cheapest value from before the stage means a lane is never credited with a jump from a lane that itself just jumped, and chains of two jumps never help because any lane is reachable from any other in a single jump.

class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        INF = float("inf")
        cost = [INF, 1, 0, 1]  # index is the lane; the frog starts in lane 2
        for blocked in obstacles[1:]:
            if blocked:
                cost[blocked] = INF
            cheapest = min(cost[1], cost[2], cost[3])
            for lane in (1, 2, 3):
                if lane != blocked and cost[lane] > cheapest + 1:
                    cost[lane] = cheapest + 1
        return min(cost[1], cost[2], cost[3])
