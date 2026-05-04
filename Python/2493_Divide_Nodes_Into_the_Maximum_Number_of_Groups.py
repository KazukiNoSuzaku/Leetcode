from collections import deque, defaultdict

class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        color = [-1] * (n + 1)
        components = []

        def bfs_color(start):
            comp = [start]
            color[start] = 0
            queue = deque([start])
            bipartite = True
            while queue:
                node = queue.popleft()
                for nei in adj[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        comp.append(nei)
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        bipartite = False
            return comp, bipartite

        def bfs_depth(start):
            dist = {start: 1}
            queue = deque([start])
            depth = 1
            while queue:
                node = queue.popleft()
                for nei in adj[node]:
                    if nei not in dist:
                        dist[nei] = dist[node] + 1
                        depth = dist[nei]
                        queue.append(nei)
            return depth

        for i in range(1, n + 1):
            if color[i] == -1:
                comp, bipartite = bfs_color(i)
                if not bipartite:
                    return -1
                components.append(comp)

        # For each component, max groups = max BFS depth from any node in it
        return sum(max(bfs_depth(node) for node in comp) for comp in components)
