# Check if people can be bipartitioned into two groups with no dislikes within a group.

# Author: Kaustav Ghosh

from collections import defaultdict, deque

class Solution(object):
    def possibleBipartition(self, n, dislikes):
        graph = defaultdict(list)
        for a, b in dislikes: graph[a].append(b); graph[b].append(a)
        color = {}
        for start in range(1, n + 1):
            if start in color: continue
            q = deque([start])
            color[start] = 0
            while q:
                node = q.popleft()
                for nb in graph[node]:
                    if nb in color:
                        if color[nb] == color[node]: return False
                    else:
                        color[nb] = 1 - color[node]
                        q.append(nb)
        return True
