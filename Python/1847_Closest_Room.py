# Author: Kaustav Ghosh
# Problem 1847: Closest Room

from sortedcontainers import SortedList

class Solution(object):
    def closestRoom(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        rooms.sort(key=lambda x: -x[1])
        indexed_queries = sorted(enumerate(queries), key=lambda x: -x[1][1])
        result = [-1] * len(queries)
        available = SortedList()
        j = 0
        for i, (preferred, minSize) in indexed_queries:
            while j < len(rooms) and rooms[j][1] >= minSize:
                available.add(rooms[j][0])
                j += 1
            if not available:
                continue
            idx = available.bisect_left(preferred)
            best = -1
            best_diff = float('inf')
            if idx < len(available):
                diff = available[idx] - preferred
                if diff < best_diff or (diff == best_diff and available[idx] < best):
                    best_diff = diff
                    best = available[idx]
            if idx > 0:
                diff = preferred - available[idx - 1]
                if diff < best_diff or (diff == best_diff and available[idx - 1] < best):
                    best_diff = diff
                    best = available[idx - 1]
            result[i] = best
        return result
