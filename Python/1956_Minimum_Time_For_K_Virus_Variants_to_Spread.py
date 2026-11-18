# Author: Kaustav Ghosh
# Problem: Minimum Time For K Virus Variants to Spread
# Approach: A variant started at (x, y) reaches a cell on day equal to their Manhattan distance, and variants do not interfere, so a cell holds k variants on the day of its k-th smallest distance to the origins. The answer is the smallest such value over all cells, and the search can be confined to the origins' bounding box: clamping a coordinate into that range never increases any |x - xi|, so no cell outside can beat the clamped one. With coordinates bounded by 100 the box holds at most 10^4 cells, and for each I keep only the k smallest distances using a heap of size k so the k-th smallest is its root. That is O(100 * 100 * n log k), comfortable for the fifty origins allowed.

import heapq

class Solution(object):
    def minDayskVariants(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        left = min(x for x, _ in points)
        right = max(x for x, _ in points)
        bottom = min(y for _, y in points)
        top = max(y for _, y in points)

        answer = None
        for a in range(left, right + 1):
            for b in range(bottom, top + 1):
                nearest = []
                for x, y in points:
                    gap = -(abs(x - a) + abs(y - b))
                    if len(nearest) < k:
                        heapq.heappush(nearest, gap)
                    elif gap > nearest[0]:
                        heapq.heapreplace(nearest, gap)
                worst = -nearest[0]
                if answer is None or worst < answer:
                    answer = worst
        return answer
