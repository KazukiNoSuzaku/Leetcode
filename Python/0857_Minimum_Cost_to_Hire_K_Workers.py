# Hire exactly k workers minimizing total wage (quality proportional, min wage satisfied).

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted((w / float(q), q) for w, q in zip(wage, quality))
        pool = []
        pool_quality = 0
        res = float('inf')
        for ratio, q in workers:
            heapq.heappush(pool, -q)
            pool_quality += q
            if len(pool) > k:
                pool_quality += heapq.heappop(pool)
            if len(pool) == k:
                res = min(res, ratio * pool_quality)
        return res
