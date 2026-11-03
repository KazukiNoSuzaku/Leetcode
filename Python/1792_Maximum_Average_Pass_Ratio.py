# Author: Kaustav Ghosh
# Problem: Maximum Average Pass Ratio
# Approach: Adding a student to a class raises its ratio by a fixed amount that only depends on that class, and crucially the gain shrinks every time the class grows, so a class is never worth a second student before some other class has had its first at the same gain. That makes the greedy choice safe: always give the next student to whichever class gains the most right now. A heap keyed on the negated gain keeps that class at hand, and the class is pushed back with its recomputed gain after each assignment.

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        from heapq import heapify, heappop, heappush

        def gain(passed, total):
            return float(passed + 1) / (total + 1) - float(passed) / total

        heap = [(-gain(passed, total), passed, total) for passed, total in classes]
        heapify(heap)
        for _ in range(extraStudents):
            _, passed, total = heappop(heap)
            passed, total = passed + 1, total + 1
            heappush(heap, (-gain(passed, total), passed, total))
        return sum(float(passed) / total for _, passed, total in heap) / len(classes)
