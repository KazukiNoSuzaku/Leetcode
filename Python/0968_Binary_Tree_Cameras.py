# Place cameras on tree nodes such that every node is monitored.
# Return the minimum number of cameras needed.

# Author: Kaustav Ghosh

class Solution(object):
    def minCameraCover(self, root):
        self.cameras = 0
        # Returns: 0 = not covered, 1 = covered no camera, 2 = has camera
        def dfs(node):
            if not node: return 1
            l, r = dfs(node.left), dfs(node.right)
            if l == 0 or r == 0:
                self.cameras += 1
                return 2
            if l == 2 or r == 2:
                return 1
            return 0
        if dfs(root) == 0:
            self.cameras += 1
        return self.cameras
