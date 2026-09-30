# Author: Kaustav Ghosh
# Problem: Minimum Score of a Path Between Two Cities
# Approach: A path may revisit cities and roads freely, so once any road is reachable from city 1 it can be walked over on the way to city n. The answer is therefore the cheapest road in city 1's connected component, found with one traversal

from collections import defaultdict


class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))
        seen = {1}
        stack = [1]
        best = float('inf')
        while stack:
            city = stack.pop()
            for nxt, distance in graph[city]:
                best = min(best, distance)
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        return best
