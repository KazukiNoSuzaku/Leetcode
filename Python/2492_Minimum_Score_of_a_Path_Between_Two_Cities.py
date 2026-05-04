from collections import deque, defaultdict

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        # The path from 1 to n can reuse edges, so any edge in the connected
        # component containing both 1 and n is reachable. Find the minimum edge weight.
        adj = defaultdict(list)
        for a, b, d in roads:
            adj[a].append((b, d))
            adj[b].append((a, d))

        visited = {1}
        queue = deque([1])
        ans = float('inf')
        while queue:
            node = queue.popleft()
            for nei, dist in adj[node]:
                ans = min(ans, dist)
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        return ans
