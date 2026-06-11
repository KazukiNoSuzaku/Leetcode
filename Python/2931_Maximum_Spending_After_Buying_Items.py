from typing import List
import heapq

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        heap = [(values[i][0], i, 0) for i in range(len(values))]
        heapq.heapify(heap)
        res = 0
        for day in range(1, len(values) * len(values[0]) + 1):
            price, i, j = heapq.heappop(heap)
            res += day * price
            if j + 1 < len(values[0]):
                heapq.heappush(heap, (values[i][j + 1], i, j + 1))
        return res
