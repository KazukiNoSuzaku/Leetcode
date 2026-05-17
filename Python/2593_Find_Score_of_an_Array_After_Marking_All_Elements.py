import heapq

class Solution:
    def findScore(self, nums: list[int]) -> int:
        marked = [False] * len(nums)
        heap = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(heap)
        score = 0
        while heap:
            v, i = heapq.heappop(heap)
            if marked[i]:
                continue
            score += v
            marked[i] = True
            if i > 0:
                marked[i - 1] = True
            if i < len(nums) - 1:
                marked[i + 1] = True
        return score
