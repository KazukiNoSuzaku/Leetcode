# Author: Kaustav Ghosh
# Problem: Number of Nodes With Value One
# Approach: Flipping a subtree twice undoes itself, so only the parity of the queries per node matters. Collapse the queries into one flip bit per node, then walk the tree from the root carrying the running parity of all flips seen on the way down, which is exactly each node's final value. The tree is the implicit heap shape, so node v's children are 2v and 2v + 1

class Solution(object):
    def numberOfNodes(self, n, queries):
        """
        :type n: int
        :type queries: List[int]
        :rtype: int
        """
        flipped = [0] * (n + 1)
        for node in queries:
            flipped[node] ^= 1
        total = 0
        stack = [(1, 0)]
        while stack:
            node, parity = stack.pop()
            parity ^= flipped[node]
            total += parity
            for child in (node * 2, node * 2 + 1):
                if child <= n:
                    stack.append((child, parity))
        return total
