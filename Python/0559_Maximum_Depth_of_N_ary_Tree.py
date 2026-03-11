# Given a n-ary tree, find its maximum depth.

# Author: Kaustav Ghosh

class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        return 1 + max((self.maxDepth(c) for c in root.children), default=0)
