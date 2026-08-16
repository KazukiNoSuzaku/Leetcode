# Author: Kaustav Ghosh
# Problem: The Time When the Network Becomes Idle
# Approach: BFS gives each server's distance to the master, so its round trip is 2*d. A server resends every patience seconds until the reply arrives at 2*d; the last resend is the largest multiple of patience strictly below 2*d. The network idles one second after the last such message returns

from collections import deque

class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        """
        n = len(patience)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        dist = [-1] * n
        dist[0] = 0
        dq = deque([0])
        while dq:
            u = dq.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    dq.append(v)

        answer = 0
        for i in range(1, n):
            round_trip = 2 * dist[i]
            p = patience[i]
            last_send = ((round_trip - 1) // p) * p
            answer = max(answer, last_send + round_trip)
        return answer + 1
