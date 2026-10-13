# Author: Kaustav Ghosh
# Problem: Min Cost to Connect All Points
# Approach: Connecting every point at least cost with no redundant edges is a minimum spanning tree, and the graph here is complete, so building the edge list explicitly would mean half a million edges for a thousand points. Prim's algorithm avoids that: it keeps for every point still outside the tree the cheapest known distance to the tree, repeatedly absorbs the nearest one, and then relaxes those distances against the newly added point, so the edge weights are computed on the fly in quadratic time with linear memory.

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        INF = float('inf')
        best = [INF] * n
        inside = [False] * n
        best[0] = 0
        total = 0
        for _ in range(n):
            # Pick the nearest point not yet in the tree.
            chosen = -1
            for i in range(n):
                if not inside[i] and (chosen < 0 or best[i] < best[chosen]):
                    chosen = i
            inside[chosen] = True
            total += best[chosen]
            cx, cy = points[chosen]
            for i in range(n):
                if not inside[i]:
                    x, y = points[i]
                    distance = abs(x - cx) + abs(y - cy)
                    if distance < best[i]:
                        best[i] = distance
        return total
