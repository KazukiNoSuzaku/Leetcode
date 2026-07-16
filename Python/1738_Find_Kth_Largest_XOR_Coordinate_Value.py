# Author: Kaustav Ghosh
# Problem: Find Kth Largest XOR Coordinate Value
# Approach: Build the 2D XOR prefix (inclusion-exclusion with XOR undoing itself) and keep the k largest values in a size-k min-heap

import heapq

class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        heap = []  # min-heap of the k largest so far

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix[i][j] = (prefix[i - 1][j] ^ prefix[i][j - 1]
                                ^ prefix[i - 1][j - 1] ^ matrix[i - 1][j - 1])
                value = prefix[i][j]
                if len(heap) < k:
                    heapq.heappush(heap, value)
                elif value > heap[0]:
                    heapq.heapreplace(heap, value)

        return heap[0]
