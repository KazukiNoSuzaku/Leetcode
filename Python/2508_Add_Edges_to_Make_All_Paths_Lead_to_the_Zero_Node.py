from collections import deque, defaultdict

class Solution:
    def addEdges(self, n: int, edges: list[list[int]]) -> int:
        # BFS on reverse graph from node 0 to find all nodes that can already reach 0.
        # Count undirected connected components among the remaining nodes; each needs one new edge.
        rev = defaultdict(list)
        for u, v in edges:
            rev[v].append(u)

        reachable = {0}
        q = deque([0])
        while q:
            node = q.popleft()
            for nb in rev[node]:
                if nb not in reachable:
                    reachable.add(nb)
                    q.append(nb)

        unreachable = set(range(n)) - reachable
        if not unreachable:
            return 0

        adj = defaultdict(list)
        for u, v in edges:
            if u in unreachable and v in unreachable:
                adj[u].append(v)
                adj[v].append(u)

        visited = set()
        components = 0
        for start in unreachable:
            if start not in visited:
                components += 1
                bfs = deque([start])
                visited.add(start)
                while bfs:
                    node = bfs.popleft()
                    for nb in adj[node]:
                        if nb not in visited:
                            visited.add(nb)
                            bfs.append(nb)

        return components
