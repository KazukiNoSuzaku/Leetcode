from typing import List
import heapq

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        result = []
        while nums:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            result.append(b)
            result.append(a)
        return result
