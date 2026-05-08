import heapq
from math import ceil

class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        # Max-heap: greedily pick the largest element k times, replacing it with ceil(val/3).
        heap = [-x for x in nums]
        heapq.heapify(heap)
        score = 0
        for _ in range(k):
            val = -heapq.heappop(heap)
            score += val
            heapq.heappush(heap, -ceil(val / 3))
        return score
