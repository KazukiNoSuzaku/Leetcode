# Author: Kaustav Ghosh
# Problem: Binary Search Tree Iterator II (Premium)
# Approach: Flatten the BST into its sorted in-order list up front, then move a cursor forward/backward for next/prev in O(1)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):
    def __init__(self, root):
        self.vals = []
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            self.vals.append(node.val)
            node = node.right
        self.pos = -1

    def hasNext(self):
        return self.pos + 1 < len(self.vals)

    def next(self):
        self.pos += 1
        return self.vals[self.pos]

    def hasPrev(self):
        return self.pos > 0

    def prev(self):
        self.pos -= 1
        return self.vals[self.pos]
