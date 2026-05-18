from collections import deque

class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start):
            dist = [-1] * n
            dist[start] = 0
            q = deque([(start, -1)])
            best = float('inf')
            while q:
                node, parent = q.popleft()
                for nb in graph[node]:
                    if dist[nb] == -1:
                        dist[nb] = dist[node] + 1
                        q.append((nb, node))
                    elif nb != parent:
                        best = min(best, dist[node] + dist[nb] + 1)
            return best

        ans = min(bfs(i) for i in range(n))
        return ans if ans != float('inf') else -1
