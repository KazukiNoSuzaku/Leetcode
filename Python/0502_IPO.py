# Suppose LeetCode will start its IPO soon. To sell a good price of its shares to Venture Capital,
# LeetCode would like to work on some projects beforehand to increase its capital.
# Given k, w, profits, capital - select at most k projects to maximize final capital.

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        available = []
        projects = sorted(zip(capital, profits))
        idx = 0
        for _ in range(k):
            while idx < len(projects) and projects[idx][0] <= w:
                heapq.heappush(available, -projects[idx][1])
                idx += 1
            if not available:
                break
            w -= heapq.heappop(available)
        return w
