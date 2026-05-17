import heapq

class Solution:
    def makePrefSumNonNegative(self, nums: list[int]) -> int:
        # Greedily move the most negative number seen so far to the end when prefix goes negative.
        heap = []  # min-heap of negative numbers encountered
        prefix = 0
        ops = 0
        for x in nums:
            if x < 0:
                heapq.heappush(heap, x)
            prefix += x
            if prefix < 0:
                # Remove the most negative element (push it to end — effectively +ops)
                most_neg = heapq.heappop(heap)
                prefix -= most_neg  # removing it repairs the prefix
                ops += 1
        return ops
