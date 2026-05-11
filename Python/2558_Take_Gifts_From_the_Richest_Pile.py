import heapq
from math import isqrt

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        # Max-heap: each operation replaces the largest pile with floor(sqrt(pile)).
        heap = [-x for x in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            largest = -heapq.heappop(heap)
            heapq.heappush(heap, -isqrt(largest))
        return -sum(heap)
