# Find the lexicographically smallest string going from leaf to root
# using node values as letters (0='a', 25='z').

# Author: Kaustav Ghosh

class Solution(object):
    def smallestFromLeaf(self, root):
        self.res = None
        def dfs(node, path):
            if not node: return
            path = chr(node.val + ord('a')) + path
            if not node.left and not node.right:
                if self.res is None or path < self.res:
                    self.res = path
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, '')
        return self.res
