# Author: Kaustav Ghosh
# Problem: Minimum Degree of a Connected Trio in a Graph
# Approach: A trio's degree is deg(u) + deg(v) + deg(w) - 6, since the three edges inside the trio are each counted by two of its endpoints, so for a fixed edge (u, v) the best third node is simply the common neighbour of lowest degree. Relabelling the nodes in increasing order of degree makes that lookup free: the common neighbours of u and v are held as a bitmask, and its lowest set bit is already the smallest-degree candidate. Every triangle is reached three times, once per edge, so scanning the edge list and taking the lowest bit of adj[u] & adj[v] finds the global minimum with one big-integer AND per edge instead of a triple loop over nodes.

class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        degree = [0] * (n + 1)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1

        order = sorted(range(1, n + 1), key=lambda node: degree[node])
        rank = [0] * (n + 1)
        for position, node in enumerate(order):
            rank[node] = position

        neighbours = [0] * n
        for u, v in edges:
            neighbours[rank[u]] |= 1 << rank[v]
            neighbours[rank[v]] |= 1 << rank[u]

        ranked_degree = [degree[node] for node in order]
        best = -1
        for u, v in edges:
            a, b = rank[u], rank[v]
            common = neighbours[a] & neighbours[b]
            if not common:
                continue
            c = (common & -common).bit_length() - 1
            total = ranked_degree[a] + ranked_degree[b] + ranked_degree[c] - 6
            if best < 0 or total < best:
                best = total
        return best
