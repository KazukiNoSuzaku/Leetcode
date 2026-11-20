# Author: Kaustav Ghosh
# Problem: Number of Ways to Arrive at Destination
# Approach: Shortest paths with non-negative weights come out of Dijkstra, and the count of shortest paths rides along with it: when a node is settled its distance is final, so every edge relaxation either beats the best known distance, in which case the path count is replaced, or ties it, in which case the counts add. Settling nodes in increasing distance order is what makes that sound, because a node's count is complete before it is ever used to relax its neighbours. I run a heap-based Dijkstra with lazy deletion, skipping heap entries whose distance is stale, and reduce the counts modulo 10^9 + 7 as they accumulate while keeping the distances themselves exact, since reducing a distance would corrupt the comparisons. Travel times reach 10^9 over up to 200 intersections, so the sums stay well inside Python's exact integers.

import heapq

class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        neighbours = [[] for _ in range(n)]
        for one, two, minutes in roads:
            neighbours[one].append((two, minutes))
            neighbours[two].append((one, minutes))

        best = [None] * n
        ways = [0] * n
        best[0] = 0
        ways[0] = 1

        heap = [(0, 0)]
        settled = [False] * n
        while heap:
            spent, here = heapq.heappop(heap)
            if settled[here]:
                continue
            settled[here] = True
            for there, minutes in neighbours[here]:
                total = spent + minutes
                if best[there] is None or total < best[there]:
                    best[there] = total
                    ways[there] = ways[here]
                    heapq.heappush(heap, (total, there))
                elif total == best[there]:
                    ways[there] = (ways[there] + ways[here]) % MOD

        return ways[n - 1]
