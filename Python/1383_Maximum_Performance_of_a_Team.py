# Author: Kaustav Ghosh
# Problem: Maximum Performance of a Team
# Approach: Sort by efficiency desc, use min-heap for speed to maintain top-k

import heapq

class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        heap = []
        speed_sum = 0
        result = 0
        for eff, spd in engineers:
            heapq.heappush(heap, spd)
            speed_sum += spd
            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)
            result = max(result, speed_sum * eff)
        return result % MOD
