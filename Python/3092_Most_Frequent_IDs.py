from typing import List
from collections import defaultdict
import heapq

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        count = defaultdict(int)
        heap = []  # max-heap via negation
        ans = []
        for num, f in zip(nums, freq):
            count[num] += f
            heapq.heappush(heap, (-count[num], num))
            # Lazy-delete stale entries
            while -heap[0][0] != count[heap[0][1]]:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans
