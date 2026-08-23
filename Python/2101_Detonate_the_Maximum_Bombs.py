# Author: Kaustav Ghosh
# Problem: Detonate the Maximum Bombs
# Approach: Build a directed graph where bomb i points to bomb j if j lies within i's blast radius. For each possible starting bomb, count the bombs reachable via DFS and return the maximum

class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        n = len(bombs)
        graph = [[] for _ in range(n)]
        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= ri * ri:
                    graph[i].append(j)

        def reachable(start):
            seen = {start}
            stack = [start]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
            return len(seen)

        return max(reachable(i) for i in range(n))
