# Author: Kaustav Ghosh
# Problem: Divide Nodes Into the Maximum Number of Groups
# Approach: Neighbours must land in adjacent groups, so the grouping is a breadth-first layering and only works when the component has no odd cycle. Within a component, starting the layering at different nodes gives different depths, and the deepest one wins; the components are independent, so sum their best depths

from collections import deque


class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n + 1)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        colour = [0] * (n + 1)
        component = [0] * (n + 1)
        components = 0
        for start in range(1, n + 1):
            if colour[start]:
                continue
            components += 1
            colour[start] = 1
            component[start] = components
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for nxt in graph[node]:
                    if not colour[nxt]:
                        colour[nxt] = -colour[node]
                        component[nxt] = components
                        queue.append(nxt)
                    elif colour[nxt] == colour[node]:
                        return -1

        deepest = [0] * (components + 1)
        for start in range(1, n + 1):
            depth = 0
            seen = {start}
            queue = deque([start])
            while queue:
                depth += 1
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for nxt in graph[node]:
                        if nxt not in seen:
                            seen.add(nxt)
                            queue.append(nxt)
            index = component[start]
            deepest[index] = max(deepest[index], depth)
        return sum(deepest)
