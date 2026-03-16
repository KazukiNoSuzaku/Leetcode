# Author: Kaustav Ghosh
# Problem: Linked List in Binary Tree
# Approach: DFS matching linked list path in tree

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        def match(node, curr):
            if not curr:
                return True
            if not node:
                return False
            if node.val != curr.val:
                return False
            return match(node.left, curr.next) or match(node.right, curr.next)

        if not root:
            return False
        return match(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
