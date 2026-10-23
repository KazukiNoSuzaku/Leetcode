# Author: Kaustav Ghosh
# Problem: Minimize Deviation in Array
# Approach: The two operations are not symmetric: an even number can be halved repeatedly but an odd one can only be doubled, and doubling it makes it even, so each number's reachable set is a chain from some maximum down to a minimum by halving. Doubling every odd value up front puts each number at the top of its own chain, after which the only useful move is to halve the current largest, since lowering anything else cannot reduce the spread. So I keep the values in a max-heap, track the smallest seen, and repeatedly halve the maximum while it is even, recording the spread each time; once the maximum is odd it can go no lower and the best spread recorded is the answer.

from heapq import heapify, heappush, heappop


class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap = []
        smallest = None
        for value in nums:
            if value % 2:
                value *= 2
            heap.append(-value)
            if smallest is None or value < smallest:
                smallest = value
        heapify(heap)

        best = -heap[0] - smallest
        while heap[0] % 2 == 0:          # negated, so this tests the real maximum
            largest = -heappop(heap)
            halved = largest // 2
            if halved < smallest:
                smallest = halved
            heappush(heap, -halved)
            spread = -heap[0] - smallest
            if spread < best:
                best = spread
        return best
