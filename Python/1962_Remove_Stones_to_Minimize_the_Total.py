# Author: Kaustav Ghosh
# Problem: Remove Stones to Minimize the Total
# Approach: Each operation removes floor(pile/2) from a pile, which is most effective on the largest pile. Use a max-heap (negated), popping the largest and pushing back the remainder k times

import heapq

class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        heap = [-p for p in piles]
        heapq.heapify(heap)
        for _ in range(k):
            largest = -heap[0]
            remain = largest - largest // 2
            heapq.heapreplace(heap, -remain)
        return -sum(heap)
