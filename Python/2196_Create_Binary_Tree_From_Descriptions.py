# Author: Kaustav Ghosh
# Problem: Create Binary Tree From Descriptions
# Approach: Create nodes on demand keyed by value, linking each parent to its child on the given side. Track every value that appears as a child; the one value that never does is the root

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        nodes = {}
        children = set()

        def get(v):
            if v not in nodes:
                nodes[v] = TreeNode(v)
            return nodes[v]

        for parent, child, is_left in descriptions:
            p = get(parent)
            c = get(child)
            if is_left:
                p.left = c
            else:
                p.right = c
            children.add(child)

        for val in nodes:
            if val not in children:
                return nodes[val]
        return None
