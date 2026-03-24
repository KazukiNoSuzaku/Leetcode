# Author: Kaustav Ghosh
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

import heapq

class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        # Max heap (negate values)
        heap = [-p for p in piles]
        heapq.heapify(heap)
        for _ in range(k):
            val = -heapq.heappop(heap)
            val -= val // 2
            heapq.heappush(heap, -val)
        return -sum(heap)
