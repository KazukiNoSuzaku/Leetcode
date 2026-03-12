# Author: Kaustav Ghosh
# 1101. The Earliest Moment When Everyone Become Friends
# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """
        parent = list(range(n))
        size = [1] * n
        components = n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            nonlocal components
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]
            components -= 1

        logs.sort()
        for timestamp, x, y in logs:
            union(x, y)
            if components == 1:
                return timestamp
        return -1
