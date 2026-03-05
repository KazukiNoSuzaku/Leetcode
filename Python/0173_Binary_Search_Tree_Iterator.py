# Implement the BSTIterator class that represents an iterator over the in-order traversal
# of a binary search tree (BST).
# - BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
# - boolean hasNext() Returns true if there exists a number in the traversal to the right.
# - int next() Moves the pointer to the right, then returns the number at the pointer.
# next() and hasNext() should run in average O(1) time and use O(h) memory, where h is the tree height.

# Example:
# Input: ["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]
#        [[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]
# Output: [null,3,7,true,9,true,15,true,20,false]

# Constraints:
# The number of nodes in the tree is in the range [1, 10^5].
# 0 <= Node.val <= 10^6

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self):
        return len(self.stack) > 0
