# Author: Kaustav Ghosh
# DFS to recover values, store in set for O(1) lookup

class FindElements(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.values = set()
        self._recover(root, 0)

    def _recover(self, node, val):
        if not node:
            return
        self.values.add(val)
        self._recover(node.left, 2 * val + 1)
        self._recover(node.right, 2 * val + 2)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.values
