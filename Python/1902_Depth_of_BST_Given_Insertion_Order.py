# Author: Kaustav Ghosh
# Problem: Depth of BST Given Insertion Order
# Approach: A newly inserted value becomes a child of whichever of its current in-order predecessor/successor was inserted deeper, so its depth is that neighbor's depth + 1. Keep inserted values sorted and track each one's depth

from sortedcontainers import SortedList

class Solution(object):
    def maxDepthBST(self, order):
        """
        :type order: List[int]
        :rtype: int
        """
        vals = SortedList()
        depth = {}
        best = 0
        for v in order:
            idx = vals.bisect_left(v)
            parent = 0
            if idx > 0:
                parent = max(parent, depth[vals[idx - 1]])
            if idx < len(vals):
                parent = max(parent, depth[vals[idx]])
            depth[v] = parent + 1
            best = max(best, depth[v])
            vals.add(v)
        return best
