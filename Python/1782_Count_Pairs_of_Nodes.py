# Author: Kaustav Ghosh

class Solution(object):
    def countPairs(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        degree = [0] * (n + 1)
        edge_count = Counter()
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            edge_count[min(u, v), max(u, v)] += 1
        sorted_deg = sorted(degree[1:])
        ans = []
        for q in queries:
            # Two pointer on sorted degrees
            count = 0
            left, right = 0, n - 1
            while left < right:
                if sorted_deg[left] + sorted_deg[right] > q:
                    count += right - left
                    right -= 1
                else:
                    left += 1
            # Subtract overcounted pairs with shared edges
            for (u, v), cnt in edge_count.items():
                if degree[u] + degree[v] > q and degree[u] + degree[v] - cnt <= q:
                    count -= 1
            ans.append(count)
        return ans
