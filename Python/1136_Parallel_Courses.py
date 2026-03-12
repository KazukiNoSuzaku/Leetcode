# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Topological sort, find longest path (minimum semesters)

class Solution(object):
    def minimumSemesters(self, n, relations):
        """
        :type n: int
        :type relations: List[List[int]]
        :rtype: int
        """
        from collections import deque, defaultdict
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        for prev, nxt in relations:
            graph[prev].append(nxt)
            indegree[nxt] += 1

        queue = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                queue.append(i)

        semesters = 0
        taken = 0
        while queue:
            semesters += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                taken += 1
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)

        return semesters if taken == n else -1
