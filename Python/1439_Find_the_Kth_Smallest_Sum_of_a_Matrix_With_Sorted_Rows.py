# Author: Kaustav Ghosh
# Problem: Find the Kth Smallest Sum of a Matrix With Sorted Rows
# Approach: Min-heap merging rows pairwise

import heapq

class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        def merge(arr1, arr2, k):
            heap = [(arr1[0] + arr2[0], 0, 0)]
            visited = {(0, 0)}
            result = []
            while heap and len(result) < k:
                s, i, j = heapq.heappop(heap)
                result.append(s)
                if i + 1 < len(arr1) and (i + 1, j) not in visited:
                    visited.add((i + 1, j))
                    heapq.heappush(heap, (arr1[i + 1] + arr2[j], i + 1, j))
                if j + 1 < len(arr2) and (i, j + 1) not in visited:
                    visited.add((i, j + 1))
                    heapq.heappush(heap, (arr1[i] + arr2[j + 1], i, j + 1))
            return result

        current = mat[0]
        for row in mat[1:]:
            current = merge(current, row, k)
        return current[k - 1]
