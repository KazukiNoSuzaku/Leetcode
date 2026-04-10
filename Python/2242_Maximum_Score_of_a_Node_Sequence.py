# Author: Kaustav Ghosh
# Problem: 2242. Maximum Score of a Node Sequence
# URL: https://leetcode.com/problems/maximum-score-of-a-node-sequence/
# Difficulty: Hard
#
# Approach:
# For each edge (u, v), try extending with the best neighbor of u (not v)
# and the best neighbor of v (not u). Keep top-3 neighbors by score for
# each node to efficiently enumerate candidates.

class Solution(object):
    def maximumScore(self, scores, edges):
        """
        :type scores: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(scores)
        # For each node, keep top 3 neighbors by score
        top = [[] for _ in range(n)]
        for u, v in edges:
            top[u].append((scores[v], v))
            top[v].append((scores[u], u))
        for i in range(n):
            top[i].sort(reverse=True)
            if len(top[i]) > 3:
                top[i] = top[i][:3]

        ans = -1
        for u, v in edges:
            for su, nu in top[u]:
                if nu == v:
                    continue
                for sv, nv in top[v]:
                    if nv == u or nv == nu:
                        continue
                    ans = max(ans, scores[u] + scores[v] + su + sv)
        return ans
