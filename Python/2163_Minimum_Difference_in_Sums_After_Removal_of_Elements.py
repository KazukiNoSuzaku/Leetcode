# Author: Kaustav Ghosh
# Problem: Minimum Difference in Sums After Removal of Elements
# Approach: The first part takes the n smallest from some prefix and the second part the n largest from the complementary suffix. Precompute, for each split point, the minimum sum of n elements on the left (max-heap) and the maximum sum of n on the right (min-heap), then minimize left minus right

import heapq

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
        n = total // 3

        prefix = [0] * (total + 1)
        heap = []
        s = 0
        for i in range(total):
            heapq.heappush(heap, -nums[i])
            s += nums[i]
            if len(heap) > n:
                s -= -heapq.heappop(heap)
            if len(heap) == n:
                prefix[i + 1] = s

        suffix = [0] * (total + 1)
        heap = []
        s = 0
        for i in range(total - 1, -1, -1):
            heapq.heappush(heap, nums[i])
            s += nums[i]
            if len(heap) > n:
                s -= heapq.heappop(heap)
            if len(heap) == n:
                suffix[i] = s

        return min(prefix[i] - suffix[i] for i in range(n, 2 * n + 1))
