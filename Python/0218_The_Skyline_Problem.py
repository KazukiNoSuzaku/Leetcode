# A city's skyline is the outer contour of the silhouette formed by all the buildings
# as viewed from a distance. Given the locations and heights of all the buildings,
# return the skyline formed by these buildings collectively.
# Each building is described by [lefti, righti, heighti].
# The skyline should be represented as a list of "critical points" [x, height].

# Example 1:
# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

# Constraints:
# 1 <= buildings.length <= 10^4
# 0 <= lefti < righti <= 2^31 - 1
# 1 <= heighti <= 2^31 - 1

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def getSkyline(self, buildings):
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        events.sort()

        result = []
        heap = [(0, float('inf'))]  # (neg_height, end)
        for x, neg_h, end in events:
            if neg_h != 0:
                heapq.heappush(heap, (neg_h, end))
            while heap[0][1] <= x:
                heapq.heappop(heap)
            curr_max = -heap[0][0]
            if result and result[-1][1] == curr_max:
                continue
            result.append([x, curr_max])
        return result
