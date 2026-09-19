# Author: Kaustav Ghosh
# Problem: Build a Matrix With Conditions
# Approach: The row conditions and the column conditions are two independent orderings of 1..k, so topologically sort each with Kahn's algorithm; a cycle in either means no matrix exists. Placing number x at (its index in the row order, its index in the column order) then satisfies both and uses each row and column exactly once

from collections import deque


class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        def topo(conditions):
            graph = [[] for _ in range(k + 1)]
            indegree = [0] * (k + 1)
            for a, b in conditions:
                graph[a].append(b)
                indegree[b] += 1
            queue = deque(x for x in range(1, k + 1) if indegree[x] == 0)
            order = []
            while queue:
                x = queue.popleft()
                order.append(x)
                for y in graph[x]:
                    indegree[y] -= 1
                    if indegree[y] == 0:
                        queue.append(y)
            return order if len(order) == k else None

        rows = topo(rowConditions)
        cols = topo(colConditions)
        if rows is None or cols is None:
            return []
        col_of = {x: i for i, x in enumerate(cols)}
        matrix = [[0] * k for _ in range(k)]
        for r, x in enumerate(rows):
            matrix[r][col_of[x]] = x
        return matrix
