# Author: Kaustav Ghosh
# Problem: Maximum Score of a Node Sequence
# Approach: A valid sequence is a path a-b-c-d over three edges. Treat each edge (b,c) as the middle edge and pick endpoints a (neighbor of b) and d (neighbor of c) with the highest scores, avoiding collisions. Keeping only each node's top-3 highest-scoring neighbors is enough, since a and d must avoid at most two already-used nodes

import heapq


class Solution(object):
    def maximumScore(self, scores, edges):
        """
        :type scores: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(scores)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # keep top-3 neighbors by score for each node
        top = []
        for node in range(n):
            best = heapq.nlargest(3, adj[node], key=lambda x: scores[x])
            top.append(best)

        ans = -1
        for b, c in edges:
            for a in top[b]:
                if a == c:
                    continue
                for d in top[c]:
                    if d == b or d == a:
                        continue
                    ans = max(ans, scores[a] + scores[b] + scores[c] + scores[d])
        return ans
