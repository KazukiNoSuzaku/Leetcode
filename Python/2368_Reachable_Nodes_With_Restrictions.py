from collections import defaultdict, deque

class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        blocked = set(restricted)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = {0}
        q = deque([0])
        while q:
            node = q.popleft()
            for nb in graph[node]:
                if nb not in visited and nb not in blocked:
                    visited.add(nb)
                    q.append(nb)
        return len(visited)
