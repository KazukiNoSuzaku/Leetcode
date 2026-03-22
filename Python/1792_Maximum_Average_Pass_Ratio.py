# Author: Kaustav Ghosh

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        import heapq
        # Max heap by gain of adding one student
        heap = []
        for p, t in classes:
            gain = (p + 1.0) / (t + 1) - float(p) / t
            heapq.heappush(heap, (-gain, p, t))
        for _ in range(extraStudents):
            neg_gain, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            gain = (p + 1.0) / (t + 1) - float(p) / t
            heapq.heappush(heap, (-gain, p, t))
        total = 0.0
        for neg_gain, p, t in heap:
            total += float(p) / t
        return total / len(classes)
