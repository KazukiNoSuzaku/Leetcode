from collections import defaultdict

class Solution:
    def maxStarSum(self, vals: list[int], edges: list[list[int]], k: int) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(vals[b])
            adj[b].append(vals[a])

        ans = max(vals)
        for i, v in enumerate(vals):
            # Add up to k positive neighbor values (sort descending, take top k)
            neighbors = sorted(adj[i], reverse=True)
            star_sum = v + sum(x for x in neighbors[:k] if x > 0)
            ans = max(ans, star_sum)
        return ans
