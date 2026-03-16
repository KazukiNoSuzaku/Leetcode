# Author: Kaustav Ghosh
# Problem: Clone N-ary Tree (Premium)
# Approach: DFS clone with children list

class Solution(object):
    def cloneTree(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        clone = Node(root.val)
        clone.children = [self.cloneTree(child) for child in root.children]
        return clone
