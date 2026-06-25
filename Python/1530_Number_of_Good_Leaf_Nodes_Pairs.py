# Author: Kaustav Ghosh
# Problem: Number of Good Leaf Nodes Pairs
# Approach: DFS returning leaf depths from current node; count cross-subtree pairs within distance, prune depths that can't contribute

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        self.ans = 0

        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.ans += 1
            return [d + 1 for d in left + right if d + 1 < distance]

        dfs(root)
        return self.ans
