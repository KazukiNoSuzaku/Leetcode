# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Two BFS - first to find farthest node, second to find diameter

class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict, deque
        if not edges:
            return 0
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start):
            visited = {start}
            queue = deque([(start, 0)])
            farthest = start
            max_dist = 0
            while queue:
                node, dist = queue.popleft()
                if dist > max_dist:
                    max_dist = dist
                    farthest = node
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, dist + 1))
            return farthest, max_dist

        far_node, _ = bfs(0)
        _, diameter = bfs(far_node)
        return diameter
