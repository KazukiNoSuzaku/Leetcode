# Author: Kaustav Ghosh
# Problem: Depth of BST Given Insertion Order
# Approach: A value inserted into a binary search tree lands as a child of whichever of its predecessor or successor among the already-present values is deeper, so its depth is one more than the larger of those two. Finding those neighbours needs an ordered structure, which Python does not supply, so the insertions are instead examined in reverse: a doubly linked list over all the values in sorted order starts complete, and removing each value as it is visited leaves exactly the values inserted before it, whose neighbours around that value are its predecessor and successor at insertion time. Both passes are linear and need nothing but arrays of indices, which avoids the quadratic cost of keeping a sorted list by insertion.

class Solution(object):
    def maxDepthBST(self, order):
        """
        :type order: List[int]
        :rtype: int
        """
        n = len(order)
        # Sentinels at 0 and n + 1 stand for "no neighbour on that side".
        before = list(range(-1, n + 1))
        after = list(range(1, n + 3))

        neighbours = [None] * (n + 1)
        for value in reversed(order):
            neighbours[value] = (before[value], after[value])
            after[before[value]] = after[value]
            before[after[value]] = before[value]

        depth = [0] * (n + 2)
        deepest = 0
        for value in order:
            lower, higher = neighbours[value]
            depth[value] = 1 + max(depth[lower], depth[higher])
            if depth[value] > deepest:
                deepest = depth[value]
        return deepest
