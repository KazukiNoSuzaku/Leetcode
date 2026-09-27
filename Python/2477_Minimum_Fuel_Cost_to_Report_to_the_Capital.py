# Author: Kaustav Ghosh
# Problem: Minimum Fuel Cost to Report to the Capital
# Approach: Every representative must cross the edge above their city, and cars can be shared freely, so the edge leading out of a subtree carries ceil(people in that subtree / seats) cars and costs that much fuel. Accumulate subtree populations upward in post-order and sum those costs

class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        n = len(roads) + 1
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        parent = [-1] * n
        order = []
        seen = [False] * n
        seen[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            order.append(node)
            for nxt in graph[node]:
                if not seen[nxt]:
                    seen[nxt] = True
                    parent[nxt] = node
                    stack.append(nxt)
        people = [1] * n
        fuel = 0
        for node in reversed(order):
            if node:
                fuel += -(-people[node] // seats)
                people[parent[node]] += people[node]
        return fuel
