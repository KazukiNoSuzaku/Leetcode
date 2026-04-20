class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        visited = [0] * len(edges)
        ans = -1
        time = 1

        for start in range(len(edges)):
            if visited[start]:
                continue
            node, t = start, time
            while node != -1 and not visited[node]:
                visited[node] = t
                t += 1
                node = edges[node]
            if node != -1 and visited[node] >= time:
                ans = max(ans, t - visited[node])
            time = t

        return ans
