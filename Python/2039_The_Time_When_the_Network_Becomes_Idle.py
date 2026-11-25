# Author: Kaustav Ghosh
# Problem: The Time When the Network Becomes Idle
# Approach: Every message travels the shortest route, so the round trip for a server is twice its edge distance from the master, which one breadth-first search from the master supplies for all servers at once. A server keeps resending at its own interval until its reply lands at the end of the round trip, so the last resend is the largest multiple of that interval strictly before the reply arrives. That final message's own reply takes another full round trip, and the server falls silent the second after it arrives, so the network's idle moment is the latest such instant across all the servers.

class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        """
        from collections import deque
        total = len(patience)
        neighbours = [[] for _ in range(total)]
        for first, second in edges:
            neighbours[first].append(second)
            neighbours[second].append(first)

        distance = [-1] * total
        distance[0] = 0
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for next_node in neighbours[node]:
                if distance[next_node] == -1:
                    distance[next_node] = distance[node] + 1
                    queue.append(next_node)

        idle = 0
        for server in range(1, total):
            trip = 2 * distance[server]
            interval = patience[server]
            last_sent = interval * ((trip - 1) // interval)
            finished = last_sent + trip + 1
            if finished > idle:
                idle = finished
        return idle
