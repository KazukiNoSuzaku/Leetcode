# Author: Kaustav Ghosh
# Problem 2097: Valid Arrangement of Pairs

from collections import defaultdict, deque

class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(deque)
        in_deg = defaultdict(int)
        out_deg = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            out_deg[start] += 1
            in_deg[end] += 1

        # Find start node for Eulerian path
        start_node = pairs[0][0]
        for node in graph:
            if out_deg[node] - in_deg[node] == 1:
                start_node = node
                break

        # Hierholzer's algorithm
        path = []
        stack = [start_node]
        while stack:
            while graph[stack[-1]]:
                nxt = graph[stack[-1]].popleft()
                stack.append(nxt)
            path.append(stack.pop())

        path.reverse()
        result = []
        for i in range(len(path) - 1):
            result.append([path[i], path[i + 1]])
        return result
