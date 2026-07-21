# Author: Kaustav Ghosh
# Problem: Maximum Average Pass Ratio
# Approach: Each extra student helps most where the marginal gain (pass+1)/(total+1) - pass/total is largest, so greedily assign via a max-heap keyed on that gain

import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        def gain(passes, total):
            return (passes + 1) / (total + 1) - passes / total

        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        return sum(p / t for _, p, t in heap) / len(classes)
