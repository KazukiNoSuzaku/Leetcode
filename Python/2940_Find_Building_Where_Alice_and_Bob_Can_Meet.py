from typing import List
import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(heights), len(queries)
        ans = [-1] * q
        pending = [[] for _ in range(n)]

        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[b] > heights[a]:
                ans[i] = b
            else:
                pending[b].append((heights[a], i))

        heap = []
        for j in range(n):
            while heap and heap[0][0] < heights[j]:
                _, idx = heapq.heappop(heap)
                ans[idx] = j
            for item in pending[j]:
                heapq.heappush(heap, item)

        return ans
