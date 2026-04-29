# Premium problem
# Complete binary tree (node i has children 2i and 2i+1).
# Each query toggles the entire subtree of a given node.
# A node ends with value 1 iff it is toggled an odd number of times.
# Use Euler tour + difference array for O(n log n).

class Solution:
    def numberOfNodes(self, n: int, queries: list[int]) -> int:
        in_t = [0] * (n + 1)
        out_t = [0] * (n + 1)
        timer = 0

        def dfs(node):
            nonlocal timer
            timer += 1
            in_t[node] = timer
            if 2 * node <= n:
                dfs(2 * node)
            if 2 * node + 1 <= n:
                dfs(2 * node + 1)
            out_t[node] = timer

        dfs(1)
        diff = [0] * (n + 2)
        for q in queries:
            diff[in_t[q]] += 1
            diff[out_t[q] + 1] -= 1

        ans = prefix = 0
        for node in range(1, n + 1):
            prefix += diff[in_t[node]]
            if prefix % 2 == 1:
                ans += 1
        return ans
