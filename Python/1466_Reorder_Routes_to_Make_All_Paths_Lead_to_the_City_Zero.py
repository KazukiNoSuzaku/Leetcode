# Author: Kaustav Ghosh
# Problem: Reorder Routes to Make All Paths Lead to the City Zero
# Approach: BFS/DFS from node 0, count edges pointing away from root

from collections import defaultdict, deque

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        roads = set()
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            roads.add((a, b))

        visited = set([0])
        queue = deque([0])
        count = 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if (node, neighbor) in roads:
                        count += 1
                    queue.append(neighbor)
        return count
