# Author: Kaustav Ghosh
# Problem 2096: Step-By-Step Directions From a Binary Tree Node to Another

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        def findPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if findPath(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if findPath(node.right, target, path):
                return True
            path.pop()
            return False

        path_to_start = []
        path_to_dest = []
        findPath(root, startValue, path_to_start)
        findPath(root, destValue, path_to_dest)

        # Remove common prefix (path to LCA)
        i = 0
        while i < len(path_to_start) and i < len(path_to_dest) and path_to_start[i] == path_to_dest[i]:
            i += 1

        # Go up from start to LCA, then down to dest
        return 'U' * (len(path_to_start) - i) + ''.join(path_to_dest[i:])
