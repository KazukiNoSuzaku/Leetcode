# Author: Kaustav Ghosh
# Problem: Maximum Cost of Trip With K Highways
# Approach: A trip is a simple path over k highways (k+1 distinct cities). With n small, use bitmask DP where dp[mask][last] is the maximum toll to have visited exactly the cities in mask ending at last. Extend to unvisited neighbors; the answer is the best dp over masks with k+1 cities set

class Solution(object):
    def maximumCost(self, n, highways, k):
        """
        :type n: int
        :type highways: List[List[int]]
        :type k: int
        :rtype: int
        """
        if k >= n:  # need k+1 distinct cities, impossible if k+1 > n
            return -1

        adj = [[] for _ in range(n)]
        for a, b, toll in highways:
            adj[a].append((b, toll))
            adj[b].append((a, toll))

        NEG = float('-inf')
        dp = [[NEG] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 0

        ans = -1
        for mask in range(1 << n):
            for last in range(n):
                cur = dp[mask][last]
                if cur == NEG:
                    continue
                if bin(mask).count('1') == k + 1:
                    ans = max(ans, cur)
                    continue
                for nxt, toll in adj[last]:
                    if not (mask >> nxt) & 1:
                        nm = mask | (1 << nxt)
                        if cur + toll > dp[nm][nxt]:
                            dp[nm][nxt] = cur + toll
        return ans
