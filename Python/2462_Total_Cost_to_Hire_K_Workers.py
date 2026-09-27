# Author: Kaustav Ghosh
# Problem: Total Cost to Hire K Workers
# Approach: Only the first and last few workers are ever candidates, so keep a min-heap of each end. Each session hires the cheaper heap top, breaking ties towards the front, and refills that side from the shrinking middle. When the two initial windows already meet there is no middle left to draw from

import heapq


class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        n = len(costs)
        front = costs[:candidates]
        back = costs[max(candidates, n - candidates):]
        heapq.heapify(front)
        heapq.heapify(back)
        low, high = candidates, n - candidates - 1
        total = 0
        for _ in range(k):
            if front and (not back or front[0] <= back[0]):
                total += heapq.heappop(front)
                if low <= high:
                    heapq.heappush(front, costs[low])
                    low += 1
            else:
                total += heapq.heappop(back)
                if low <= high:
                    heapq.heappush(back, costs[high])
                    high -= 1
        return total
