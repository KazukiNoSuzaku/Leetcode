# Author: Kaustav Ghosh
# Problem: Remove Stones to Minimize the Total
# Approach: Each operation removes floor(pile / 2) stones from one pile, so the gain of an operation is larger for larger piles, and taking from the current largest pile is optimal: the halving is monotone, so no sequence that skips today's biggest pile can ever remove more in total than one that takes it. That makes this a straightforward greedy over a max-heap, which Python gives by storing negated pile sizes, popping the biggest, and pushing back what remains after the removal. Each of the k operations costs one heap replacement, so the whole thing is O((n + k) log n).

import heapq

class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        for _ in range(k):
            biggest = -heap[0]
            if biggest <= 1:
                break
            heapq.heapreplace(heap, -(biggest - biggest // 2))
        return -sum(heap)
