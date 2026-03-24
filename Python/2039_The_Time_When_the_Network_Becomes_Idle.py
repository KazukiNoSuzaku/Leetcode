# Author: Kaustav Ghosh
# Problem 2039: The Time When the Network Becomes Idle

from collections import deque

class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        """
        n = len(patience)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # BFS from node 0 to find shortest distances
        dist = [-1] * n
        dist[0] = 0
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for nei in adj[node]:
                if dist[nei] == -1:
                    dist[nei] = dist[node] + 1
                    queue.append(nei)
        ans = 0
        for i in range(1, n):
            round_trip = 2 * dist[i]
            # Last resend time before reply arrives
            if round_trip % patience[i] == 0:
                last_resend = round_trip - patience[i]
            else:
                last_resend = round_trip - (round_trip % patience[i])
            # Last message arrives at last_resend + round_trip
            ans = max(ans, last_resend + round_trip + 1)
        return ans
