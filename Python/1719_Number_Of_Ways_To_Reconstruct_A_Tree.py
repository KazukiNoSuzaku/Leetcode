# Author: Kaustav Ghosh
# Problem: Number Of Ways To Reconstruct A Tree
# Approach: A pair records that one node is an ancestor of the other, so a node's pair count is its depth plus its subtree size less one, which means an ancestor always has at least as many pairs as its descendant and the root must be paired with every other node. Sorting the nodes by pair count and letting each take as parent the first later node in that order which it is paired with therefore finds a consistent parent, and sorting is what breaks ties between equal counts the same way every time, leaving exactly one node at the top with no parent. Validity then reduces to containment: everything paired with a node must also be paired with its parent, since a node's ancestors and descendants are all ancestors or descendants of the parent as well. When a node and its parent have equal counts their roles can be swapped without altering any pair, and that is the only source of a second arrangement.

from collections import defaultdict


class Solution(object):
    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        adjacent = defaultdict(set)
        for x, y in pairs:
            adjacent[x].add(y)
            adjacent[y].add(x)

        nodes = sorted(adjacent, key=lambda v: len(adjacent[v]))
        n = len(nodes)
        multiple = False
        topmost = 0

        for i, x in enumerate(nodes):
            own = len(adjacent[x])
            parent = None
            # The first node ordered after x that x is paired with.
            for j in range(i + 1, n):
                if nodes[j] in adjacent[x]:
                    parent = nodes[j]
                    break
            if parent is None:
                # Nothing can sit above x, so x must be paired with everything.
                if own != n - 1:
                    return 0
                topmost += 1
                continue
            for z in adjacent[x]:
                if z != parent and z not in adjacent[parent]:
                    return 0
            if len(adjacent[parent]) == own:
                multiple = True

        if topmost != 1:
            return 0
        return 2 if multiple else 1
