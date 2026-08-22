# Author: Kaustav Ghosh
# Problem: Step-By-Step Directions From a Binary Tree Node to Another
# Approach: Find the L/R path from the root to each target. Drop the shared prefix (their lowest common ancestor); the answer goes up from start to the LCA ('U' per remaining start step) then follows the destination's remaining path

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
        def path_to(value):
            stack = [(root, [])]
            while stack:
                node, path = stack.pop()
                if node.val == value:
                    return path
                if node.left:
                    stack.append((node.left, path + ['L']))
                if node.right:
                    stack.append((node.right, path + ['R']))
            return []

        start_path = path_to(startValue)
        dest_path = path_to(destValue)

        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1

        return 'U' * (len(start_path) - i) + ''.join(dest_path[i:])
