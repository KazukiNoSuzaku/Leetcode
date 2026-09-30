# Author: Kaustav Ghosh
# Problem: Add Edges to Make Degrees of All Nodes Even
# Approach: Each added edge flips the parity of two nodes, so with at most two edges only zero, two or four odd-degree nodes can ever be fixed. Two odd nodes are joined directly, or routed through any third node that neighbours neither; four odd nodes must split into two disjoint pairs, so try the three pairings

class Solution(object):
    def isPossible(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        neighbours = [set() for _ in range(n + 1)]
        for a, b in edges:
            neighbours[a].add(b)
            neighbours[b].add(a)
        odd = [node for node in range(1, n + 1) if len(neighbours[node]) % 2]
        if not odd:
            return True
        if len(odd) == 2:
            a, b = odd
            if b not in neighbours[a]:
                return True
            return any(node not in neighbours[a] and node not in neighbours[b]
                       for node in range(1, n + 1) if node != a and node != b)
        if len(odd) == 4:
            a, b, c, d = odd
            return ((b not in neighbours[a] and d not in neighbours[c])
                    or (c not in neighbours[a] and d not in neighbours[b])
                    or (d not in neighbours[a] and c not in neighbours[b]))
        return False
