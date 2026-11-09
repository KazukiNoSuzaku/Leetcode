# Author: Kaustav Ghosh
# Problem: Largest Color Value in a Directed Graph
# Approach: Along any path the tally of each colour only grows, so for each node it is enough to know, per colour, the largest tally achievable on a path ending there, which is twenty-six numbers rather than a list of paths. Those tallies are built in topological order, since a node's own figures are final only once every predecessor has contributed, and each node then adds one to its own colour before passing its row on. Kahn's algorithm supplies that order and also detects the cycle case for free: if it fails to emit every node the graph has a cycle and no path value is bounded, which is the -1 answer.

class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import deque

        n = len(colors)
        outgoing = [[] for _ in range(n)]
        incoming = [0] * n
        for source, destination in edges:
            outgoing[source].append(destination)
            incoming[destination] += 1

        tallies = [[0] * 26 for _ in range(n)]
        queue = deque(node for node in range(n) if incoming[node] == 0)
        emitted = 0
        best = 0
        while queue:
            node = queue.popleft()
            emitted += 1
            row = tallies[node]
            row[ord(colors[node]) - 97] += 1
            own = max(row)
            if own > best:
                best = own
            for nxt in outgoing[node]:
                target = tallies[nxt]
                for colour in range(26):
                    if row[colour] > target[colour]:
                        target[colour] = row[colour]
                incoming[nxt] -= 1
                if incoming[nxt] == 0:
                    queue.append(nxt)
        return best if emitted == n else -1
