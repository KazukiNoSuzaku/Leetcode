# Author: Kaustav Ghosh
# Problem: Diameter of N-Ary Tree
# Approach: The longest path bends at exactly one node, where it joins that node's two deepest branches, so walk the tree in post-order keeping each node's height. Combining the two largest child heights at every node and taking the best covers every possible bend. The walk uses an explicit stack since the tree may be 1000 deep

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution(object):
    def diameter(self, root):
        """
        :type root: 'Node'
        :rtype: int
        """
        order = []
        stack = [root]
        while stack:
            node = stack.pop()
            order.append(node)
            stack.extend(node.children)

        height = {}
        best = 0
        for node in reversed(order):
            tallest = second = 0
            for child in node.children:
                reach = height[child] + 1
                if reach > tallest:
                    tallest, second = reach, tallest
                elif reach > second:
                    second = reach
            height[node] = tallest
            best = max(best, tallest + second)
        return best
