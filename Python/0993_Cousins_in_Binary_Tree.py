# Two nodes are cousins if they have the same depth but different parents.
# Return true if nodes x and y are cousins.

# Author: Kaustav Ghosh

class Solution(object):
    def isCousins(self, root, x, y):
        self.dx = self.dy = self.px = self.py = None
        def dfs(node, parent, depth):
            if not node: return
            if node.val == x: self.dx, self.px = depth, parent
            if node.val == y: self.dy, self.py = depth, parent
            dfs(node.left, node.val, depth + 1)
            dfs(node.right, node.val, depth + 1)
        dfs(root, None, 0)
        return self.dx == self.dy and self.px != self.py
