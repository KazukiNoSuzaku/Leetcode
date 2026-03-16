# Author: Kaustav Ghosh
# Problem: Construct Target Array With Multiple Sums
# Approach: Reverse simulation with max-heap

import heapq

class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)
        while True:
            largest = -heapq.heappop(heap)
            if largest == 1:
                return True
            rest = total - largest
            if rest == 0 or rest >= largest:
                return False
            if rest == 1:
                return True
            prev = largest % rest
            if prev == 0:
                return False
            total = rest + prev
            heapq.heappush(heap, -prev)
