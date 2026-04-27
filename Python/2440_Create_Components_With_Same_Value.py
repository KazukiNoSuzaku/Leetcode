from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

class Solution:
    def componentValue(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        total = sum(nums)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent, target):
            s = nums[node]
            for nb in adj[node]:
                if nb != parent:
                    child = dfs(nb, node, target)
                    if child == -1:
                        return -1
                    s += child
            if s > target:
                return -1
            return 0 if s == target else s

        for k in range(n, 0, -1):
            if total % k == 0 and dfs(0, -1, total // k) == 0:
                return k - 1
        return 0
