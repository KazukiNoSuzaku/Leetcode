# Author: Kaustav Ghosh
# Problem: Furthest Building You Can Reach
# Approach: Save ladders for the biggest climbs via a min-heap; when climbs exceed ladders, pay bricks for the smallest one, stopping when bricks run out

import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        climbs = []  # min-heap of gaps currently covered by ladders
        for i in range(len(heights) - 1):
            gap = heights[i + 1] - heights[i]
            if gap > 0:
                heapq.heappush(climbs, gap)
                if len(climbs) > ladders:
                    bricks -= heapq.heappop(climbs)
                    if bricks < 0:
                        return i
        return len(heights) - 1
