# Author: Kaustav Ghosh
# Problem 2065: Maximum Path Quality of a Graph

class Solution(object):
    def maximalPathQuality(self, values, edges, maxTime):
        """
        :type values: List[int]
        :type edges: List[List[int]]
        :type maxTime: int
        :rtype: int
        """
        n = len(values)
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        ans = [0]
        visited = [False] * n
        visited[0] = True

        def dfs(node, time_left, quality):
            if node == 0:
                ans[0] = max(ans[0], quality)
            for nei, t in adj[node]:
                if t <= time_left:
                    was_visited = visited[nei]
                    if not was_visited:
                        visited[nei] = True
                    dfs(nei, time_left - t, quality + (0 if was_visited else values[nei]))
                    if not was_visited:
                        visited[nei] = False

        dfs(0, maxTime, values[0])
        return ans[0]
