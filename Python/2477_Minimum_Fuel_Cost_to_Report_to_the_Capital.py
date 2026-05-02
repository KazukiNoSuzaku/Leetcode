import math
from collections import defaultdict

class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        adj = defaultdict(list)
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)

        total_fuel = 0

        def dfs(node, parent) -> int:
            nonlocal total_fuel
            people = 1  # this node sends one representative
            for nei in adj[node]:
                if nei != parent:
                    people += dfs(nei, node)
            if node != 0:
                total_fuel += math.ceil(people / seats)
            return people

        dfs(0, -1)
        return total_fuel
