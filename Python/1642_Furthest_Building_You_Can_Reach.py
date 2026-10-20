# Author: Kaustav Ghosh
# Problem: Furthest Building You Can Reach
# Approach: Ladders are unlimited in height, so they should always end up on the largest climbs, but which climbs are largest is not known until they have been seen. So I spend a ladder on every climb as it arrives and keep those climbs in a min-heap; once more ladders are in use than exist, the smallest of them is demoted to bricks, which is exactly the swap that keeps ladders on the biggest climbs seen so far. Running out of bricks at a climb means it cannot be crossed at all, and the previous building is as far as the journey goes. Descents and level moves are free and simply skipped.

from heapq import heappush, heappop


class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        on_ladders = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            heappush(on_ladders, climb)
            if len(on_ladders) > ladders:
                bricks -= heappop(on_ladders)
                if bricks < 0:
                    return i
        return len(heights) - 1
