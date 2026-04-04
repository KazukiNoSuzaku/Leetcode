# Author: Kaustav Ghosh

from collections import defaultdict, deque

class Solution(object):
    def getAncestors(self, n, edges):
        # type: (int, List[List[int]]) -> List[List[int]]
        children = defaultdict(list)
        parents = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            children[u].append(v)
            parents[v].append(u)
            indegree[v] += 1

        # Topological sort (Kahn's algorithm)
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        ancestors = [set() for _ in range(n)]

        while queue:
            node = queue.popleft()
            for child in children[node]:
                ancestors[child].add(node)
                ancestors[child].update(ancestors[node])
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        return [sorted(ancestors[i]) for i in range(n)]
