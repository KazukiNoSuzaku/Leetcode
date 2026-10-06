# Author: Kaustav Ghosh
# Problem: Number of Good Leaf Nodes Pairs
# Approach: Every leaf pair meets at exactly one node, so walk the tree in post-order carrying the depths of the leaves below each node. At a node with two subtrees, pair their depth lists and count the sums within the limit, then pass the depths up with one added, dropping any that already exceed the limit

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: Optional[TreeNode]
        :type distance: int
        :rtype: int
        """
        order = []
        stack = [root]
        while stack:
            node = stack.pop()
            order.append(node)
            for child in (node.left, node.right):
                if child:
                    stack.append(child)

        depths = {}
        total = 0
        for node in reversed(order):
            children = [child for child in (node.left, node.right) if child]
            if not children:
                depths[node] = [1]
                continue
            if len(children) == 2:
                for a in depths[children[0]]:
                    for b in depths[children[1]]:
                        if a + b <= distance:
                            total += 1
            depths[node] = [d + 1 for child in children for d in depths[child]
                            if d + 1 <= distance]
        return total
